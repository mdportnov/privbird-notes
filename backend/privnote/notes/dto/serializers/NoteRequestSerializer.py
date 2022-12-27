from __future__ import annotations

from django.utils.translation import gettext_lazy as _
from drf_yasg.openapi import Schema, TYPE_OBJECT
from rest_framework import serializers

from notes.dto.request.NoteCreateRequest import NoteCreateRequest
from notes.dto.serializers.NoteSerializer import NoteSerializer
from notes.dto.serializers.OptionsSerializer import OptionsSerializer


class NoteRequestSerializer(serializers.Serializer):
    note = NoteSerializer()
    fake = NoteSerializer()
    options = OptionsSerializer()

    def validate(self, attrs):
        request: NoteCreateRequest = NoteCreateRequest.deserialize(attrs)

        if request.note.content is None:
            raise serializers.ValidationError({'note': {'content': _('This field may not be null.')}})

        if request.note.password is None:
            if request.fake.password:
                raise serializers.ValidationError({'fake': {'password': _('This field must be null.')}})

        if request.note.notification is None:
            raise serializers.ValidationError({'note': {'content': _('This field may not be null.')}})

        if request.fake.content is None:
            if request.fake.password:
                raise serializers.ValidationError({'fake': {'password': _('This field must be null.')}})

            if request.fake.notification:
                raise serializers.ValidationError({'fake': {'notification': _('This field must be null.')}})

        if request.fake.content:
            if request.note.password:
                if request.fake.password is None:
                    raise serializers.ValidationError({'fake': {'password': _('This field may not be null.')}})

            if request.fake.notification is None:
                raise serializers.ValidationError({'fake': {'notification': _('This field may not be null.')}})

        if request.options.email is None:
            if request.note.notification or request.fake.notification:
                raise serializers.ValidationError({'options': {'email': _('This field may not be null.')}})

        return request

    @classmethod
    def api_schema(cls) -> Schema:
        return Schema(
            title=cls.__name__,
            type=TYPE_OBJECT,
            properties={
                'note': NoteSerializer.api_schema(),
                'fake': NoteSerializer.api_schema(),
                'options': OptionsSerializer.api_schema(),
            }
        )
