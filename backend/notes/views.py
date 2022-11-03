import json

from rest_framework import generics, mixins, status
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from notes.messages.NoteCreated import NoteCreatedMessage
from notes.models import Note
from notes.serializers.PostNoteRequestSerializer import PostNoteRequestSerializer
from privbird.messages.MessageSerializer import MessageSerializer


class PostNoteView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Note.objects.all()
    serializer_class = PostNoteRequestSerializer

    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            note = serializer.create(serializer.validated_data)
            data = json.dumps({'slug': note.slug})
            message = MessageSerializer(NoteCreatedMessage(data))
            return Response(message.data, status=status.HTTP_201_CREATED)
        raise ValidationError()


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
