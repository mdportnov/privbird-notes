from typing import Dict

from rest_framework import serializers

from notes.dto.request.CreateNoteRequest import CreateNoteRequest
from notes.dto.serializers.NoteOptionsRequestSerializer import NoteOptionsRequestSerializer
from notes.dto.serializers.NoteRequestSerializer import NoteRequestSerializer


class CreateNoteRequestSerializer(serializers.Serializer):
    note = NoteRequestSerializer()
    fake = NoteRequestSerializer()
    options = NoteOptionsRequestSerializer()

    def validate(self, attrs: Dict) -> Dict:
        data = super().validate(attrs)
        CreateNoteRequest.deserialize(data).validate()
        return data
