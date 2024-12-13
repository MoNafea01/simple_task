from rest_framework import serializers
# from ai_operations.models import TrainTestSplit
# from ai_operations.models import User

# class TrainTestSplitSerializer(serializers.Serializer):
#     data = serializers.ListField(child=serializers.FloatField())
#     test_size = serializers.FloatField(default=0.2)
#     random_state = serializers.IntegerField(allow_null=True,required=False)

#     class Meta:
#         model = TrainTestSplit
#         fields = (
#             'test_size',
#             'random_state',
#         )




class TrainTestSplitSerializer(serializers.Serializer):
    X = serializers.ListField(child=serializers.ListField(child=serializers.FloatField()))
    y = serializers.ListField(child=serializers.FloatField())
    test_size = serializers.FloatField()
    random_state = serializers.IntegerField(required=False)

class StandardScalerSerializer(serializers.Serializer):
    data = serializers.ListField(child=serializers.ListField(child=serializers.FloatField()))


class LogisticRegressionSerializer(serializers.Serializer):
    X_train = serializers.ListField(child=serializers.ListField(child=serializers.FloatField()))
    y_train = serializers.ListField(child=serializers.FloatField())


class AccuracyScoreSerializer(serializers.Serializer):
    y_true = serializers.ListField(child=serializers.FloatField())
    y_pred = serializers.ListField(child=serializers.FloatField())


class ModelFitSerializer(serializers.Serializer):
    model = serializers.CharField()
    X = serializers.ListField(child=serializers.ListField(child=serializers.FloatField()))


class ModelPredictSerializer(serializers.Serializer):
    model = serializers.CharField()
    X = serializers.ListField(child=serializers.ListField(child=serializers.FloatField()))

class ScalerFitTransformSerializer(serializers.Serializer):
    data = serializers.ListField(child=serializers.ListField(child=serializers.FloatField()))