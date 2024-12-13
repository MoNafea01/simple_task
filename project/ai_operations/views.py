from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
#from sklearn.model_selection import train_test_split

import numpy as np
from .utils import *
from .serializers import *
# Create your views here.


# @api_view(['POST'])
# def train_test_split_view(request):
#     data = request.data.get('data', [])
#     test_size = request.data.get('test_size', 0.2)
#     random_state = request.data.get('random_state', None)

#     try:
#         # Convert data to numpy array
#         X = np.array(data)
        
#         # Perform train-test split
#         X_train, X_test = train_test_split(X, test_size=test_size, random_state=random_state)
        
#         # Convert numpy arrays back to lists for JSON serialization
#         return Response({
#             'X_train': X_train.tolist(),
#             'X_test': X_test.tolist()
#         })
#     except Exception as e:
#         return Response({'error': str(e)},status=400)
    

# # @api_view(['GET'])
# # def getRoutes(request):
# #     routes = [
        
# #     ]

@api_view(['GET'])
def home(request):
    return Response({"message": "Home"})

@api_view(['GET'])
def room1(request):
    return HttpResponse('This is a room') 


@api_view(['POST'])
def execute_function(request):
    # import logging
    # logger = logging.getLogger(__name__)

    # logger.info(f"Request method: {request.method}")
    # logger.info(f"Request data: {request.data}")
    # logger.info(f"Request body: {request.body}")

    # print(f"Request method: {request.method}")
    # print(f"Request data: {request.data}")
    # print(f"Request body: {request.body}")

    if request.method == 'GET':
        return JsonResponse({"available_functions": list(function_map.keys())}, status=200)

    function_name = request.data.get("function_name")
    data = request.data.get("data")

    if not function_name or not data:
        return JsonResponse({"error": "Invalid request. 'function_name' and 'data' are required."}, status=status.HTTP_400_BAD_REQUEST)
    
    try:

        function_map = {
            "train_test_split": (perform_train_test_split, TrainTestSplitSerializer),
            "standard_scaler": (perform_standard_scaler, StandardScalerSerializer),
            "logistic_regression": (perform_logistic_regression, LogisticRegressionSerializer),
            "accuracy_score": (calculate_accuracy_score, AccuracyScoreSerializer),
            "model_predict": (perform_model_predict, ModelFitSerializer),
            "model_fit": (perform_model_fit, ModelPredictSerializer),
            "scaler_fit_transform": (perform_scaler_fit_transform, ScalerFitTransformSerializer),
            #"scaler_transform": (perform_scaler_transform, None),
            # "load_iris": (load_iris_data, None),  # Example without serializer
            # "print": (perform_print, PrintSerializer),
        }

        if function_name not in function_map:
            return JsonResponse({"error": f"Function '{function_name}' not supported."})
        

        func, serializer_class = function_map[function_name]


        if serializer_class:
            serializer = serializer_class(data=data)
            if not serializer.is_valid():
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            validated_data = serializer.validated_data
        
        else:
            validated_data = data

        if function_name == "train_test_split":
            result = func(data=validated_data, test_size=validated_data.get("test_size"), random_state=validated_data.get("random_state"))

        else:    
            result = func(**validated_data)
        return JsonResponse({"result": result}, status = status.HTTP_200_OK)
    

    except Exception as e:
        return JsonResponse({"error": str(e)}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    

