from rest_framework import serializers

class TrainTestSplitSerializer(serializers.Serializer):
    data = serializers.ListField(child=serializers.FloatField())
    test_size = serializers.FloatField(default=0.2)
    random_state = serializers.IntegerField(allow_null=True,required=False)