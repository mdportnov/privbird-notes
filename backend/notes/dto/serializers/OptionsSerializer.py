from drf_yasg.openapi import Schema, TYPE_OBJECT, TYPE_STRING
from rest_framework import serializers

from notes.models import Note
from notes.utils.Expires import Expires


class OptionsSerializer(serializers.Serializer):
    network = serializers.ChoiceField(choices=Note.Network.choices, default=Note.Network.HTTPS)
    expires = serializers.ChoiceField(choices=Expires, default=Expires.YEAR)
    email = serializers.EmailField(allow_null=True, default=None)

    @classmethod
    def api_schema(cls) -> Schema:
        return Schema(
            title=cls.__name__,
            type=TYPE_OBJECT,
            properties={
                'network': Schema(
                    type=TYPE_STRING,
                    enum=[str(network) for network in Note.Network]
                ),
                'expires': Schema(
                    type=TYPE_STRING,
                    enum=[str(expires) for expires in Expires]
                ),
                'email': Schema(type=TYPE_STRING),
            }
        )
