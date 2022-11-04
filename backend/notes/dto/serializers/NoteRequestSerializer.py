from typing import Dict

from drf_yasg.openapi import Schema, TYPE_OBJECT
from rest_framework import serializers

from notes.dto.request.CreateNoteRequest import CreateNoteRequest
from notes.dto.serializers.NoteSerializer import NoteSerializer
from notes.dto.serializers.OptionsSerializer import OptionsSerializer


class NoteRequestSerializer(serializers.Serializer):
    note = NoteSerializer()
    fake = NoteSerializer()
    options = OptionsSerializer()

    def validate(self, attrs: Dict) -> Dict:
        data = super().validate(attrs)
        CreateNoteRequest.deserialize(data).validate()
        return data

    @property
    def validated_data(self) -> CreateNoteRequest:
        return CreateNoteRequest.deserialize(super().validated_data)

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
