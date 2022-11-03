from rest_framework import serializers

from notes.models import Note
from notes.utils.expiration import Expiration


class OptionsSerializer(serializers.Serializer):
    network = serializers.ChoiceField(choices=Note.Network.choices, default=Note.Network.HTTPS)
    expires = serializers.ChoiceField(choices=Expiration, default=Expiration.YEAR)
    email = serializers.EmailField(allow_null=True, default=None)
