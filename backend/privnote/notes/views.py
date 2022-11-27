from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.views import APIView

from notes.dto.exceptions.NoteNotFound import NoteNotFoundException
from notes.dto.exceptions.PasswordRequired import PasswordRequiredException
from notes.dto.messages.NoteCreatedMessage import NoteCreatedMessage
from notes.dto.messages.NoteRetrievedMessage import NoteRetrievedMessage
from notes.dto.request.CreateNoteRequest import CreateNoteRequest
from notes.dto.request.PasswordRequest import PasswordRequest
from notes.dto.serializers.NoteRequestSerializer import NoteRequestSerializer
from notes.dto.serializers.PasswordSerializer import PasswordSerializer
from notes.models import Note
from privnote.utils.serializers import get_validated_data


def find_note_by_slug(slug: str):
    """
    Find Note entity by slug
    """

    if not Note.objects.filter(slug=slug).exists():
        raise NoteNotFoundException()
    return Note.objects.get(slug=slug)


class CreateNoteView(APIView):
    @swagger_auto_schema(
        request_body=NoteRequestSerializer.api_schema(),
        responses={status.HTTP_200_OK: NoteCreatedMessage.api_schema()}
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
        - If the `note.password` is passed, it cannot be null.
        - If the `note.password` is not passed, it must be null.
        - If different from the note password, the note will be deleted immediately after the **first** time\
        someone reads the note.
        - If the `fake.content` is not passed, it must be null.

        `note.notification` (optional) if true, a notification will be sent by mail when someone reads the fake note.
        - If the `fake.content` is passed, it cannot be null.
        - If the `fake.content` is not passed, it must be null.

        ---

        ## Options
        `options.network` defines the network over which this note will be transmitted.

        `options.expires` defines the time after which the note will be deleted if no one reads it.

        `options.email` (optional) defines the email address to which messages about reading the note will be sent.
        - If at least one flag from `note.notification` or `fake.notification` is set to true, it cannot be null.
        """

        note_request: CreateNoteRequest = get_validated_data(NoteRequestSerializer, request.data)
        note = note_request.validate_and_save()
        slug = f'{note.slug}/{note.key}' if note.key else note.slug
        return NoteCreatedMessage(slug).as_json_response()


class NoteKeyView(APIView):
    @swagger_auto_schema(
        operation_id='notes_read_with_key',
        responses={status.HTTP_200_OK: NoteRetrievedMessage.api_schema()}
    )
    def get(self, request: Request, slug: str, key: str) -> JsonResponse:
        """
        # Get note by slug without password
        The content of the note will be destroyed.
        - If there is no fake content, the note will be destroyed after the first reading.
        - If there is fake content, it will be returned next time and the note will also be destroyed.
        """
        note = find_note_by_slug(slug)
        if note.real_password or note.fake_password:
            raise PasswordRequiredException()
        content = note.get_content(key)
        return NoteRetrievedMessage(content).as_json_response()


class NotePasswordView(APIView):
    serializer_class = PasswordSerializer

    @swagger_auto_schema(
        operation_id='notes_read_with_password',
        request_body=PasswordSerializer.api_schema(),
        responses={status.HTTP_200_OK: NoteRetrievedMessage.api_schema()}
    )
    def post(self, request: Request, slug: str) -> JsonResponse:
        """
        # Get note by slug with password
        The content of the note will be destroyed.
        - If there is no fake content, the note will be destroyed after the first reading.
        - If there is fake content, it will be returned next time and the note will also be destroyed.
        """

        note = find_note_by_slug(slug)
        request: PasswordRequest = get_validated_data(PasswordSerializer, request.data)
        content = note.get_content(request.password)
        return NoteRetrievedMessage(content).as_json_response()
