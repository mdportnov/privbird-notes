import json
from typing import Dict, Optional
from unittest import TestCase

from django.http import JsonResponse
from rest_framework import status
from rest_framework.test import APIRequestFactory

from notes.views import CreateNoteView, NoteView


class NoteTestCase(TestCase):
    factory = APIRequestFactory()
    note = {
        'content': 'content',
        'password': None,
        'notification': False
    }
    options = {
        'network': 'HTTPS',
        'expires': 'Expires.YEAR',
        'email': None
    }

    def note_create(self, data: Dict) -> JsonResponse:
        request = self.factory.post('/api/notes/', data, format='json')
        view = CreateNoteView.as_view()
        return view(request)

    def note_retrieve(self, slug: str, password: Optional[str] = None) -> JsonResponse:
        request = self.factory.get(f'/api/notes/{slug}/')
        view = NoteView.as_view()
        return view(request)

    def test_note_create(self):
        data = {
            'note': self.note,
            'fake': self.note,
            'options': self.options
        }
        response = self.note_create(data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_note_retrieve(self):
        data = {
            'note': self.note,
            'fake': self.note,
            'options': self.options
        }
        slug = json.loads(self.note_create(data).content)['data']['slug']
        response = self.note_retrieve(slug)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
