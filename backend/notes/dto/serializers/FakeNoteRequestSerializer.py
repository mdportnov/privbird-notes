from rest_framework import serializers

from notes.utils.constants import Constants


class FakeNoteRequestSerializer(serializers.Serializer):
    content = serializers.CharField(max_length=Constants.MAX_CONTENT_LENGTH, allow_null=True, default=None)
    password = serializers.CharField(allow_null=True, default=None)
    notification = serializers.BooleanField(allow_null=True, default=None)
