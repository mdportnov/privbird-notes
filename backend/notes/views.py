from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from notes.dto.request.CreateNoteRequest import CreateNoteRequest
from notes.dto.serializers.CreateNoteRequestSerializer import CreateNoteRequestSerializer
from notes.messages.NoteCreated import NoteCreatedMessage
from notes.models import Note


class PostNoteView(APIView):
    serializer_class = CreateNoteRequestSerializer

    def get_note_request(self, request: Request) -> CreateNoteRequest:
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        return CreateNoteRequest.deserialize(serializer.validated_data)

    def post(self, request: Request, *args, **kwargs) -> Response:
        note_request = self.get_note_request(request)
        note = note_request.save_as_note()
        message = NoteCreatedMessage({'slug': note.slug}).serialize()
        return Response(message, status=status.HTTP_201_CREATED)


class NoteView(APIView):
    def get(self, request: Request, slug: str) -> Response:
        content = Note.find_by_slug(slug)
        return Response({'content': content})

    def post(self, request: Request, slug: str) -> Response:
        if 'password' not in request.data:
            raise ValidationError({'password': 'This field must be passed.'})
        password = request.data['password']
        content = Note.find_by_slug_and_password(slug, password)
        return Response({'content': content})
