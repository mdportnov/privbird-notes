from rest_framework import serializers

from notes.utils.constants import Constants


class NoteRequestSerializer(serializers.Serializer):
    content = serializers.CharField(max_length=Constants.MAX_CONTENT_LENGTH)
    password = serializers.CharField(allow_null=True, default=None)
    notification = serializers.BooleanField(default=False)