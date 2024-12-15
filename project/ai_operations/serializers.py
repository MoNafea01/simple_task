# api/serializers.py
from rest_framework import serializers
from .models import Workflow, Node




class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = '__all__'

class WorkflowSerializer(serializers.ModelSerializer):
    nodes = NodeSerializer(many=True)

    class Meta:
        model = Workflow
        fields = ['id', 'name', 'description', 'nodes']

class ModelSerializer(serializers.Serializer):
    model_name = serializers.CharField(max_length=100)
    model_type = serializers.CharField(max_length=100)
    task = serializers.CharField(max_length=100)
    params = serializers.JSONField()

class FitModelSerializer(serializers.Serializer):
    X = serializers.JSONField(required=False)
    y = serializers.JSONField(required=False)
    model = serializers.JSONField(
        required=True,
        help_text="Model identifier or path."
    )

class PredictSerializer(serializers.Serializer):
    X = serializers.JSONField(required=False)
    model = serializers.JSONField()

class PreprocessorSerializer(serializers.Serializer):
    preprocessor_name = serializers.ChoiceField(choices=['standard_scaler', 'minmax_scaler', 'robust_scaler', 'normalizer'])  # Add all supported scalers
    preprocessor_type = serializers.ChoiceField(choices=['scaler', 'encoding', 'imputation', 'binarization'])
    params = serializers.JSONField(required=False)

class FitPreprocessorSerializer(serializers.Serializer):
    data = serializers.JSONField()
    preprocessor = serializers.JSONField()

class TransformSerializer(serializers.Serializer):
    data = serializers.JSONField()
    preprocessor = serializers.JSONField(required=False, allow_null=True, help_text="preprocessor as JSON object.")

class FitTransformSerializer(serializers.Serializer):
    data = serializers.JSONField()
    preprocessor = serializers.JSONField(required=False, allow_null=True, help_text="preprocessor as JSON object or path.")
    
class SplitterSerializer(serializers.Serializer):
    data = serializers.JSONField()

class TrainTestSplitSerializer(serializers.Serializer):
    data = serializers.JSONField()
    test_size = serializers.FloatField(
        required=False,
        help_text="Proportion of the dataset to include in the test split."
    )
    random_state = serializers.IntegerField(
        required=False,
        help_text="Random state for reproducibility."
    )
