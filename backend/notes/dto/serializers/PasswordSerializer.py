from rest_framework import serializers

from notes.dto.request.PasswordRequest import PasswordRequest


class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField()

    @property
    def validated_data(self) -> PasswordRequest:
        return PasswordRequest.deserialize(super().validated_data)
