from rest_framework import serializers

from notes.serializers.dto.CreateNoteRequest import CreateNoteRequest


def validate_fake_data(attrs):
    request = CreateNoteRequest(**attrs)

    if request.fakePassword is not None:
        if request.fakeContent is None:
            raise serializers.ValidationError({'fakePassword': 'This field may not be null.'})

    if request.fakeNotification is None:
        if request.fakeContent is not None:
            raise serializers.ValidationError({'fakeNotification': 'This field may not be null.'})

    if request.fakeNotification is not None:
        if request.fakeContent is None:
            raise serializers.ValidationError({'fakeNotification': 'This field must be null.'})

    if request.email is None:
        if request.notification is True or attrs['fakeNotification'] is True:
            raise serializers.ValidationError({'email': 'This field may not be null.'})
