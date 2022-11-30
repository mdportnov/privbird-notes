from __future__ import annotations

from drf_yasg.openapi import Schema, TYPE_OBJECT
from rest_framework import serializers

from notes.dto.request.CreateNoteRequest import CreateNoteRequest
from notes.dto.serializers.NoteSerializer import NoteSerializer
from notes.dto.serializers.OptionsSerializer import OptionsSerializer
from notes.models import Note


class NoteRequestSerializer(serializers.Serializer):
    note = NoteSerializer()
    fake = NoteSerializer()
    options = OptionsSerializer()

    def validate_and_save(self) -> Note:
        data: NoteRequestSerializer = self.validated_data
        note = Note(
            real_content=data.note.content,
            real_password=data.note.password,
            real_notification=data.note.notification,

            fake_content=data.fake.content,
            fake_password=data.fake.password,
            fake_notification=data.fake.notification,

            expires=data.options.expires.get_expiration(),
            email=data.options.email
        )
        note.save()
        return note

    def validate(self, attrs):
        request: CreateNoteRequest = CreateNoteRequest.deserialize(attrs)

        if request.note.content is None:
            raise serializers.ValidationError({'note': {'content': 'This field may not be null.'}})

        if request.note.password is None:
            if request.fake.password:
                raise serializers.ValidationError({'fake': {'password': 'This field must be null.'}})

        if request.note.notification is None:
            raise serializers.ValidationError({'note': {'content': 'This field may not be null.'}})

        if request.fake.content is None:
            if request.fake.password:
                raise serializers.ValidationError({'fake': {'password': 'This field must be null.'}})

            if request.fake.notification:
                raise serializers.ValidationError({'fake': {'notification': 'This field must be null.'}})

        if request.fake.content:
            if request.note.password:
                if request.fake.password is None:
                    raise serializers.ValidationError({'fake': {'password': 'This field may not be null.'}})

            if request.fake.notification is None:
                raise serializers.ValidationError({'fake': {'notification': 'This field may not be null.'}})

        if request.options.email is None:
            if request.note.notification or request.fake.notification:
                raise serializers.ValidationError({'options': {'email': 'This field may not be null.'}})

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
