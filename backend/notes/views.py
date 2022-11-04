from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.views import APIView

from notes.dto.request.CreateNoteRequest import CreateNoteRequest
from notes.dto.serializers.ContentSerializer import ContentSerializer
from notes.dto.serializers.NoteRequestSerializer import NoteRequestSerializer
from notes.dto.serializers.PasswordSerializer import PasswordSerializer
from notes.messages.NoteCreated import NoteCreatedMessage
from notes.models import Note
from privbird.messages.ApiMessage import ApiMessage


class CreateNoteView(APIView):
    queryset = Note.objects.all()
    serializer_class = NoteRequestSerializer

    def get_note_request(self, request: Request) -> CreateNoteRequest:
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        return serializer.validated_data

    @swagger_auto_schema(
        request_body=NoteRequestSerializer.api_schema(),
        responses={status.HTTP_200_OK: ApiMessage.api_schema()}
    )
    def post(self, request: Request, *args, **kwargs) -> JsonResponse:
        """
        # Create note
        ## Note
        `note.content` will be returned the **first** time someone reads the note, and then immediately deleted.

        `note.password` (optional) will be used to encrypt and decrypt the note content.

        `note.notification` if true, a notification will be sent by mail when someone reads the note.

        ---

        ## Fake
        `fake.content` (optional) will be returned the **second** time someone reads the note,\
        and then immediately deleted.

        `fake.password` (optional) will be used to encrypt and decrypt the note content.
        - If different from the note password, the note will be deleted immediately after the **first** time\
        someone reads the note.
        - If the `fake.content` is not passed, it must be null.

        `note.notification` (optional) if true, a notification will be sent by mail when someone reads the fake note.
        - If the `fake.content` is passed, it cannot be null.
        - If the `fake.content` is not passed, it must be null.

        ---

        ## Options
        `options.network` defines the network over which this note will be transmitted.

        `options.language` defines the language of email messages.

        `options.expires` defines the time after which the note will be deleted if no one reads it.

        `options.email` defines the email address to which messages about reading the note will be sent.
        - If at least one flag from `note.notification` or `fake.notification` is set to true, it cannot be null.
        """

        note_request = self.get_note_request(request)
        note = note_request.save_as_note()
        message = NoteCreatedMessage({'slug': note.slug}).serialize()
        return JsonResponse(message, status=status.HTTP_201_CREATED)


class NoteView(APIView):
    serializer_class = PasswordSerializer

    @swagger_auto_schema(
        operation_id='note_get_without_password',
        responses={status.HTTP_200_OK: ContentSerializer.api_schema()}
    )
    def get(self, request: Request, slug: str) -> JsonResponse:
        """
        # Get note by slug without password
        The content of the note will be destroyed.
        - If there is no fake content, the note will be destroyed after the first reading.
        - If there is fake content, it will be returned next time and the note will also be destroyed.
        """

        content = Note.find_by_slug(slug)
        response = ContentSerializer({'content': content}).data
        return JsonResponse(response)

    @swagger_auto_schema(
        operation_id='note_get_with_password',
        responses={status.HTTP_200_OK: ContentSerializer.api_schema()}
    )
    def post(self, request: Request, slug: str) -> JsonResponse:
        """
        # Get note by slug with password
        The content of the note will be destroyed.
        - If there is no fake content, the note will be destroyed after the first reading.
        - If there is fake content, it will be returned next time and the note will also be destroyed.
        """

        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        password = serializer.validated_data.password
        content = Note.find_by_slug_and_password(slug, password)
        response = ContentSerializer({'content': content}).data
        return JsonResponse(response)
