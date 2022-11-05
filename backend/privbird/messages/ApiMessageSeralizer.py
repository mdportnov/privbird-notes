from rest_framework import serializers


class ApiMessageSerializer(serializers.Serializer):
    class MessageSerializer(serializers.Serializer):
        ru = serializers.CharField()
        en = serializers.CharField()

    message = MessageSerializer()
    data = serializers.Field()
