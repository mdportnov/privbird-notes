from rest_framework import serializers


class GetNoteRequestSerializer(serializers.Serializer):
    password = serializers.CharField()
