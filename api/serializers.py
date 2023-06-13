from rest_framework import serializers

class TextSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=1000)
    country = serializers.CharField(max_length=10)