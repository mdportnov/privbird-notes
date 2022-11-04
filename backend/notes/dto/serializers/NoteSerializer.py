from drf_yasg.openapi import Schema, TYPE_BOOLEAN, TYPE_OBJECT, TYPE_STRING
from rest_framework import serializers

from notes.utils.Constants import Constants


class NoteSerializer(serializers.Serializer):
    content = serializers.CharField(allow_null=True, default=None, max_length=Constants.MAX_CONTENT_LENGTH)
    password = serializers.CharField(allow_null=True, default=None)
    notification = serializers.BooleanField(allow_null=True, default=None)

    @classmethod
    def api_schema(cls) -> Schema:
        return Schema(
            title=cls.__name__,
            type=TYPE_OBJECT,
            properties={
                'content': Schema(type=TYPE_STRING),
                'password': Schema(type=TYPE_STRING),
                'notification': Schema(type=TYPE_BOOLEAN),
            }
        )
