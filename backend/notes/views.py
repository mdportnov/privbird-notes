from django.http import JsonResponse
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from notes.dto.request.CreateNoteRequest import CreateNoteRequest
from notes.dto.serializers.NoteRequestSerializer import NoteRequestSerializer
from notes.dto.serializers.PasswordSerializer import PasswordSerializer
from notes.messages.NoteCreated import NoteCreatedMessage
from notes.models import Note


class PostNoteView(APIView):
    serializer_class = NoteRequestSerializer

    def get_note_request(self, request: Request) -> CreateNoteRequest:
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        return serializer.validated_data

    def post(self, request: Request, *args, **kwargs) -> JsonResponse:
        note_request = self.get_note_request(request)
        note = note_request.save_as_note()
        message = NoteCreatedMessage({'slug': note.slug}).serialize()
        return JsonResponse(message, status=status.HTTP_201_CREATED)


class NoteView(APIView):
    serializer_class = PasswordSerializer

    def get(self, request: Request, slug: str) -> JsonResponse:
        content = Note.find_by_slug(slug)
        return JsonResponse({'content': content})

    def post(self, request: Request, slug: str) -> JsonResponse:
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        password = serializer.validated_data.password
        content = Note.find_by_slug_and_password(slug, password)
        return JsonResponse({'content': content})
