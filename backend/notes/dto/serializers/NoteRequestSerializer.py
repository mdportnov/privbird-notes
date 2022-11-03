from typing import Dict

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
