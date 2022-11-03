from rest_framework import serializers

from notes.models import Note
from notes.serializers.dto.CreateNoteRequest import CreateNoteRequest
from notes.serializers.validators.validate_fake_data import validate_fake_data
from notes.utils.constants import Constants
from notes.utils.expiration import Expiration


class PostNoteRequestSerializer(serializers.ModelSerializer):
    content = serializers.CharField(max_length=Constants.MAX_CONTENT_LENGTH)
    password = serializers.CharField(allow_null=True, default=None)
    notification = serializers.BooleanField(default=False)

    fakeContent = serializers.CharField(allow_null=True, default=None)
    fakePassword = serializers.CharField(allow_null=True, default=None)
    fakeNotification = serializers.BooleanField(allow_null=True, default=False)

    network = serializers.ChoiceField(choices=Note.Network.choices, default=Note.Network.HTTPS)
    expires = serializers.ChoiceField(choices=Expiration, default=Expiration.YEAR)
    email = serializers.EmailField(allow_null=True, default=None)

    class Meta:
        model = Note
        fields = [
            'content', 'password', 'notification',
            'fakeContent', 'fakePassword', 'fakeNotification',
            'network', 'expires', 'email'
        ]

    def validate(self, attrs) -> serializers.Serializer:
        validate_fake_data(attrs)
        return super().validate(attrs)

    def create(self, validated_data) -> Note:
        request = CreateNoteRequest(**validated_data)
        validated_data['expires'] = validated_data['expires'].get_expiration()
        if request.password != request.fakePassword:
            validated_data['fakeContent'] = None
        return super().create(validated_data)
