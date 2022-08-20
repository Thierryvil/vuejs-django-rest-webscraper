from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    image = serializers.CharField()
    thumbnail = serializers.CharField()
    valueFrom = serializers.FloatField()
    valueTo = serializers.FloatField()
