from rest_framework import serializers


class ExceptionSerializer(serializers.Serializer):
    en = serializers.CharField()
    ru = serializers.CharField()
    status_code = serializers.IntegerField()
    timestamp = serializers.DateTimeField()
    errors = serializers.CharField()
