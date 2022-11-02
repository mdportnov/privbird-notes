from re import search

from django.contrib.auth.hashers import check_password
from django.contrib.messages import add_message, ERROR
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseNotFound
from django.utils.timezone import now

from drf_yasg.openapi import Schema, TYPE_OBJECT, TYPE_STRING
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status

from .models import Note, Option, Support
from .serializers import NoteSerializer, SupportSerializer
from bruteforce.protection import Attempt


def validate_content(content):
    return content is not None


def validate_choices(type_choice, auto_destruction_choice):
    option = Option()
    return type_choice in [choice[0] for choice in option.type_choices] and (
            auto_destruction_choice in [choice[0] for choice in option.auto_destruction_choices])


def validate_password(password):
    return password is None or (password is not None and len(password) > 7)


def validate_notification(main, fake):
    return type(main) == bool and type(fake) == bool


def validate_email(email):
    return email is None or (
        email is not None and search(r'^[A-Za-z0-9_!#$%&\'*+/=?`{|}~^.-]+@[A-Za-z0-9.-]+$', email))


def validate_fake_note(fake_note):
    if fake_note is not None:
        return validate_content(fake_note['content']) and validate_password(fake_note['password'])
    
    return True


def validate_note_data(data):
    return validate_content(data['content']) and (
        validate_choices(data['option']['type'], data['option']['auto_destruction'])) and (
        validate_password(data['option']['password'])) and (
        validate_notification(data['option']['notification']['main'], data['option']['notification']['fake'])) and (
        validate_email(data['option']['notification']['email'])) and (
        validate_fake_note(data['option']['fake_note']))


def validate_support_data(data):
    return validate_content(data['problem']) and validate_email(data['option']['notification']['email'])


class IndexView(generics.GenericAPIView):
    @swagger_auto_schema(
        operation_id = 'notes_create',
        operation_description = 'Go to home page',
        operation_summary = 'Go to home page',
        responses = {
            status.HTTP_200_OK: Schema(
                title = 'Home',
                description = 'Home page',
                type = TYPE_STRING,
            ),
        },
        tags = ['Index'],
    )
    def get(self, request, *args, **kwargs):
        return HttpResponse(status = status.HTTP_200_OK)


class HomeView(generics.GenericAPIView):
    model = Note
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    
    @swagger_auto_schema(
        operation_id = 'notes_create',
        operation_description = 'Create note',
        operation_summary = 'Create note',
        responses = {
            status.HTTP_200_OK: Schema(
                title = 'Home',
                description = 'Home page',
                type = TYPE_STRING,
            ),
        },
        tags = ['Home'],
    )
    def get(self, request, *args, **kwargs):
        return HttpResponse(status = status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body = NoteSerializer,
        operation_id = 'notes_create',
        operation_description = 'Create note',
        operation_summary = 'Create note',
        responses = {
            status.HTTP_201_CREATED: Schema(
                title = 'Link',
                description = 'Note link',
                type = TYPE_STRING,
            ),
            status.HTTP_400_BAD_REQUEST: Schema(
                title = 'Error',
                description = 'Validation error',
                type = TYPE_STRING,
            ),
        },
        tags = ['Home'],
    )
    def post(self, request, *args, **kwargs):
        if not validate_note_data(request.data):
            return HttpResponse(status = status.HTTP_400_BAD_REQUEST)
        
        note = Note.objects.get_or_create(**request.data).prepare_content()
        link = request.build_absolute_uri(note.get_absolute_url())
        return HttpResponse(link, status = status.HTTP_201_CREATED)


class NoteView(generics.GenericAPIView):
    model = Note
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'slug'
    
    message = {
        'error': {
            'en': 'You entered the wrong password... Try again!',
            'ru': 'Вы ввели неправильный пароль... Попробуйте еще раз!',
        }
    }
    
    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.option.expiration_time < now() or (
                object.option.confirmation and object.option.password != object.option.fake_note.password) or (
                object.option.confirmation > 1 and object.option.password == object.option.fake_note.password) or (
                object.option.confirmation and not object.option.falsification):
            return HttpResponseNotFound('Note is not found')
        
        return super().dispatch(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_id = 'notes_read',
        operation_description = 'Read note',
        operation_summary = 'Read note',
        responses = {
            status.HTTP_200_OK: Schema(
                title = 'Content',
                description = 'Note content',
                type = TYPE_STRING,
            ),
            status.HTTP_401_UNAUTHORIZED: Schema(
                title = 'Error',
                description = 'Authorization error',
                type = TYPE_STRING,
            ),
            status.HTTP_404_NOT_FOUND: Schema(
                title = 'Error',
                description = 'Note is not found',
                type = TYPE_STRING,
            ),
        },
        tags = ['Note'],
    )
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if check_password('', self.object.option.password):
            content = self.object.manage_content()
            return HttpResponse(content, status = status.HTTP_200_OK)
        
        return HttpResponse(status = status.HTTP_401_UNAUTHORIZED)
    
    @swagger_auto_schema(
        request_body = Schema(
            type = TYPE_OBJECT,
            properties = {
                'password': Schema(type = TYPE_STRING),
            },
        ),
        operation_id = 'notes_read',
        operation_description = 'Read password-protected note',
        operation_summary = 'Read password-protected note',
        responses = {
            status.HTTP_200_OK: Schema(
                title = 'Content',
                description = 'Note content',
                type = TYPE_STRING,
            ),
            status.HTTP_400_BAD_REQUEST: Schema(
                title = 'Error',
                description = 'Validation error',
                type = TYPE_STRING,
            ),
            status.HTTP_403_FORBIDDEN: Schema(
                title = 'Error',
                description = 'Authentication error',
                type = TYPE_STRING,
            ),
            status.HTTP_404_NOT_FOUND: Schema(
                title = 'Error',
                description = 'Note is not found',
                type = TYPE_STRING,
            ),
        },
        tags = ['Note'],
    )
    def post(self, request, *args, **kwargs):
        if not request.session.get('load_count'):
            request.session['load_count'] = 1
        
        attempt = Attempt(request, request.session['load_count'])
        if not attempt.check():
            request.session['load_count'] += 1
            return HttpResponse(attempt.error, status = status.HTTP_403_FORBIDDEN)
        
        self.object = self.get_object()
        password = request.data['password']
        if not validate_password(password):
            return HttpResponse(status = status.HTTP_400_BAD_REQUEST)
        
        return self.process(request, password, *args, **kwargs)
    
    def process(self, request, password, *args, **kwargs):
        try:
            content = self.object.get_content(password)
        except PermissionDenied as error:
            add_message(request, ERROR, error)
            return HttpResponse(self.message['error']['en'], status = status.HTTP_403_FORBIDDEN)
        
        return HttpResponse(content, status = status.HTTP_200_OK)


class SupportView(generics.GenericAPIView):
    model = Support
    queryset = Support.objects.all()
    serializer_class = SupportSerializer
    
    @swagger_auto_schema(
        operation_id = 'support_create',
        operation_description = 'Go to support page',
        operation_summary = 'Go to support page',
        responses = {
            status.HTTP_200_OK: Schema(
                title = 'Support',
                description = 'Support page',
                type = TYPE_STRING,
            ),
        },
        tags = ['Support'],
    )
    def get(self, request, *args, **kwargs):
        return HttpResponse(status = status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body = SupportSerializer,
        operation_id = 'support_create',
        operation_description = 'Contact support',
        operation_summary = 'Contact support',
        responses = {
            status.HTTP_201_CREATED: Schema(
                title = 'Support',
                description = 'Support page',
                type = TYPE_STRING,
            ),
        },
        tags = ['Support'],
    )
    def post(self, request, *args, **kwargs):
        if not validate_support_data(request.data):
            return HttpResponse(status = status.HTTP_400_BAD_REQUEST)
        
        Support.objects.create(**request.data)
        return HttpResponse(status = status.HTTP_201_CREATED)