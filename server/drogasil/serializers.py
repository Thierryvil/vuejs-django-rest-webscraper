from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    image = serializers.CharField()
    thumbnail = serializers.CharField()
    valueFrom = serializers.FloatField()
    valueTo = serializers.FloatField()


    def validate(self, validated_data):
        if validated_data['image']:
            validated_data['image'] = f"https:{validated_data['image']}"
        if validated_data['thumbnail']:
            validated_data['thumbnail'] = f"https:{validated_data['thumbnail']}"
        return validated_data
