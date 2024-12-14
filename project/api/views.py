from django.shortcuts import render

# Create your views here.
# api/views.py
from rest_framework import viewsets
from rest_framework.response import Response
# from .models import Workflow
from rest_framework.decorators import action, api_view
from rest_framework.views import APIView, Response
from rest_framework import status
from core.nodes import DataLoader
from core.nodes.model.model import Model
from core.nodes.model.fit import Fit as FitModel
from core.nodes.model.predict import Predict
from core.nodes.preprocessing.transformer import Scaler
from core.nodes.preprocessing.transform import Transform
from core.nodes.preprocessing.splitter import TrainTestSplit
from core.nodes.preprocessing.fit_transform import FitTransform
from core.nodes.preprocessing.fit import Fit as FitScaler
from core.nodes.metrics import Evaluator
from .serializers import WorkflowSerializer, ModelSerializer, FitModelSerializer, PredictSerializer, ScalerSerializer
from .serializers import FitScalerSerializer, TransformSerializer, FitTransformSerializer, TrainTestSplitSerializer
from .models import Workflow

class WorkflowViewSet(viewsets.ModelViewSet):
    queryset = Workflow.objects.all()
    serializer_class = WorkflowSerializer

    @action(detail=True, methods=['post'])
    def execute(self, request, pk=None):
        workflow = self.get_object()
        nodes = workflow.nodes.order_by('order')

        # Here, execute the nodes sequentially
        result = self.execute_workflow(nodes)
        return Response({"result": result}, status=status.HTTP_200_OK)

    def execute_workflow(self,nodes):
        # Load data
        for node in nodes:
            if node.node_type == "dataLoader":
                loader = DataLoader(**node.config)
                X, y = loader.load()

            elif node.node_type == "splitter":
                splitter = TrainTestSplit(**node.config).payload.values()
                (X_train, X_test), (y_train, y_test) = splitter

            elif node.node_type == "transformer":
                scaler = Scaler(**node.config)
            
            elif node.node_type == "fit_transform":
                X_train = FitTransform(X_train, scaler).payload['transformed_data']
            elif node.node_type == "transform":
                X_test = Transform(X_test, scaler).payload['transformed_data']
            elif node.node_type == "model":
                model = Model(**node.config)
            elif node.node_type == "fit":
                FitModel(X_train, y_train, model)
            elif node.node_type == "predict":
                y_pred = Predict(X_test, model).payload['predictions']
            elif node.node_type == "evaluator":
                evaluator = Evaluator(**node.config)
                score = evaluator.evaluate(y_test, y_pred)
        return score


@api_view(['POST'])
def create_model(request):
    if request.method == 'POST':
        serializer = ModelSerializer(data=request.data)
        if serializer.is_valid():
            # Extract data from the serializer
            data = serializer.validated_data
            # Create Model instance using the data
            model_instance = Model(
                model_name=data['model_name'],
                model_type=data['model_type'],
                task=data['task'],
                params=data['params']
            )
            return Response(model_instance(), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FitModelAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = FitModelSerializer(data=request.data)
        if serializer.is_valid():
            X = serializer.validated_data['X']
            y = serializer.validated_data['y']
            model = serializer.validated_data['model']

            try:
                # Fit the model
                fitter = FitModel(X, y, model=model)
                response_data = fitter()  # Get the JSON-serializable payload
                return Response(response_data, status=status.HTTP_200_OK)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PredictAPIView(APIView):
    """
    API view to handle predictions using a trained model.
    """

    def post(self, request, *args, **kwargs):
        serializer = PredictSerializer(data=request.data)
        if serializer.is_valid():
            X = serializer.validated_data['X']
            model = serializer.validated_data['model']

            try:
                # Perform prediction
                predictor = Predict(X, model=model)
                response_data = predictor()  # Get the JSON-serializable payload
                return Response(response_data, status=status.HTTP_200_OK)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ScalerAPIView(APIView):
    """
    API view to create a scaler instance.
    """

    def post(self, request, *args, **kwargs):
        serializer = ScalerSerializer(data=request.data)
        if serializer.is_valid():
            scaler_name = serializer.validated_data['scaler_name']
            params = serializer.validated_data.get('params', {})

            try:
                # Create the scaler
                scaler = Scaler(scaler_name, params=params)
                response_data = scaler()  # Get the JSON-serializable payload
                return Response(response_data, status=status.HTTP_200_OK)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class FitScalerAPIView(APIView):
    """
    API view for fitting a transformer on the given data.
    """

    def post(self, request, *args, **kwargs):
        serializer = FitScalerSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data['data']
            transformer = serializer.validated_data.get('transformer')

            try:
                # Create a Fit instance
                fit_instance = FitScaler(data=data, transformer=transformer)
                response_data = fit_instance()  # Get the JSON-serializable payload
                return Response(response_data, status=status.HTTP_200_OK)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransformAPIView(APIView):
    """
    API view for transforming data using the given transformer.
    """

    def post(self, request, *args, **kwargs):
        # Deserialize input data using the serializer
        serializer = TransformSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data['data']
            transformer = serializer.validated_data.get('transformer')  # Extract transformer (as JSON object)

            try:
                # Create a Transform instance and get the result
                transform_instance = Transform(data=data, transformer=transformer)
                response_data = transform_instance()  # Get the JSON-serializable payload
                return Response(response_data, status=status.HTTP_200_OK)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FitTransformAPIView(APIView):
    """
    API view for fitting and transforming data using the given transformer.
    """

    def post(self, request, *args, **kwargs):
        # Deserialize input data using the serializer
        serializer = FitTransformSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data['data']
            transformer = serializer.validated_data.get('transformer')  # Extract transformer (as JSON object or path)

            try:
                # Create a FitTransform instance and get the result
                fit_transform_instance = FitTransform(data=data, transformer=transformer)
                response_data = fit_transform_instance()  # Get the JSON-serializable payload
                return Response(response_data, status=status.HTTP_200_OK)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class TrainTestSplitAPIView(APIView):
    """
    API view for splitting data into training and test sets.
    """

    def post(self, request, *args, **kwargs):
        # Deserialize the incoming data using the serializer
        serializer = TrainTestSplitSerializer(data=request.data)
        if serializer.is_valid():
            data = {
                'X': serializer.validated_data['X'],
                'y': serializer.validated_data['y']
            }
            test_size = serializer.validated_data['test_size']
            random_state = serializer.validated_data.get('random_state', None)

            try:
                # Create the TrainTestSplit instance and process the data
                split_instance = TrainTestSplit(data, test_size=test_size, random_state=random_state)
                response_data = split_instance()  # Get the result as a dictionary
                return Response(response_data, status=status.HTTP_200_OK)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

