from drf_yasg.openapi import Schema, TYPE_OBJECT, TYPE_STRING
from rest_framework import serializers


class ContentSerializer(serializers.Serializer):
    content = serializers.CharField()

    @classmethod
    def api_schema(cls) -> Schema:
        return Schema(
            title=cls.__name__,
            type=TYPE_OBJECT,
            properties={
                'content': Schema(type=TYPE_STRING)
            }
        )
