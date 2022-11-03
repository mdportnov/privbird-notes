from rest_framework import serializers

from notes.dto.serializers.FakeNoteRequestSerializer import FakeNoteRequestSerializer
from notes.dto.serializers.NoteOptionsRequestSerializer import NoteOptionsRequestSerializer
from notes.dto.serializers.NoteRequestSerializer import NoteRequestSerializer


class PostNoteRequestSerializer(serializers.Serializer):
    note = NoteRequestSerializer()
    fake = FakeNoteRequestSerializer()
    options = NoteOptionsRequestSerializer()
