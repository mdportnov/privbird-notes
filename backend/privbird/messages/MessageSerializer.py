from rest_framework import serializers


class MessageSerializer(serializers.Serializer):
    en = serializers.CharField()
    ru = serializers.CharField()
    data = serializers.CharField()
