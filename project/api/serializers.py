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
    X = serializers.ListField(
        child=serializers.ListField(
            child=serializers.FloatField(),
            min_length=1
        ),
        min_length=1
    )
    y = serializers.ListField(
        child=serializers.FloatField(),
        min_length=1
    )
    model = serializers.JSONField()

class PredictSerializer(serializers.Serializer):
    X = serializers.ListField(
        child=serializers.ListField(
            child=serializers.FloatField(),
            min_length=1
        ),
        min_length=1
    )
    model = serializers.JSONField()

class ScalerSerializer(serializers.Serializer):
    scaler_name = serializers.ChoiceField(choices=['standard_scaler', 'minmax_scaler', 'robust_scaler'])  # Add all supported scalers
    params = serializers.DictField(child=serializers.FloatField(), required=False)

class FitScalerSerializer(serializers.Serializer):
    data = serializers.ListField(
        child=serializers.ListField(child=serializers.FloatField()),
        help_text="2D list representing the data to be transformed."
    )
    transformer = serializers.JSONField()

class TransformSerializer(serializers.Serializer):
    data = serializers.ListField(
        child=serializers.ListField(child=serializers.FloatField()),
        help_text="2D list representing the data to be transformed."
    )
    transformer = serializers.JSONField(required=False, allow_null=True, help_text="Transformer as JSON object.")

class FitTransformSerializer(serializers.Serializer):
    data = serializers.ListField(
        child=serializers.ListField(child=serializers.FloatField()),
        help_text="2D list representing the data to be transformed."
    )
    transformer = serializers.JSONField(required=False, allow_null=True, help_text="Transformer as JSON object or path.")

class TrainTestSplitSerializer(serializers.Serializer):
    X = serializers.ListField(
        child=serializers.ListField(child=serializers.FloatField()),
        help_text="Input features (X) as a 2D list of floats."
    )
    y = serializers.ListField(
        child=serializers.FloatField(),
        help_text="Labels (y) as a list of floats."
    )
    test_size = serializers.FloatField(default=0.25, min_value=0.0, max_value=1.0, help_text="Fraction of data to use for the test set.")
    random_state = serializers.IntegerField(required=False, allow_null=True, help_text="Random state for reproducibility.")

