from drf_yasg.openapi import Schema, TYPE_OBJECT, TYPE_STRING
from rest_framework import serializers

from notes.dto.request.PasswordRequest import PasswordRequest


class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField()

    @property
    def validated_data(self) -> PasswordRequest:
        return PasswordRequest.deserialize(super().validated_data)

    @classmethod
    def api_schema(cls) -> Schema:
        return Schema(
            title=cls.__name__,
            type=TYPE_OBJECT,
            properties={
                'password': Schema(title='password', type=TYPE_STRING),
            }
        )
