import json
from secrets import token_hex
from typing import Dict, Optional, Tuple
from unittest import TestCase

from django.http import JsonResponse
from rest_framework import status
from rest_framework.test import APIClient

URL = '/privnote/api'


def generate_note_request(
        real_content: str = token_hex(),
        real_password: Optional[str] = None,
        fake_content: Optional[str] = None,
        fake_password: Optional[str] = None
) -> Dict:
    return {
        'note': {
            'content': real_content,
            'password': real_password,
            'notification': False
        },
        'fake': {
            'content': fake_content,
            'password': fake_password,
            'notification': False if fake_content else None
        },
        'options': {
            'network': 'HTTPS',
            'expires': 'YEAR',
            'email': None
        }
    }


def create(data: Dict) -> Tuple[int, str]:
    client = APIClient()
    response: JsonResponse = client.post(f'{URL}/notes/', data, format='json')
    message = json.loads(response.content)
    content = message['data']['slug'] if 200 <= response.status_code <= 299 else None
    return response.status_code, content


class NoteCreateTestCase(TestCase):
    def test_none_real_content(self):
        request = generate_note_request()
        request['note']['content'] = None
        code, _ = create(request)
        self.assertEqual(code, status.HTTP_400_BAD_REQUEST)

    def test_none_real_notification(self):
        request = generate_note_request()
        request['note']['notification'] = None
        code, _ = create(request)
        self.assertEqual(code, status.HTTP_400_BAD_REQUEST)

    def test_none_fake_notification(self):
        request = generate_note_request(fake_content=token_hex())
        request['fake']['notification'] = None
        code, _ = create(request)
        self.assertEqual(code, status.HTTP_400_BAD_REQUEST)

    def test_none_email_real_notification(self):
        request = generate_note_request()
        request['note']['notification'] = True
        request['options']['email'] = None
        code, _ = create(request)
        self.assertEqual(code, status.HTTP_400_BAD_REQUEST)

    def test_none_email_fake_notification(self):
        request = generate_note_request(fake_content=token_hex())
        request['fake']['notification'] = True
        request['options']['email'] = None
        code, _ = create(request)
        self.assertEqual(code, status.HTTP_400_BAD_REQUEST)

    def test_none_fake_password(self):
        request = generate_note_request(fake_content=token_hex())
        request['note']['password'] = token_hex()
        request['fake']['password'] = None
        code, _ = create(request)
        self.assertEqual(code, status.HTTP_400_BAD_REQUEST)

    def test_none_real_passwords(self):
        request = generate_note_request(fake_content=token_hex())
        request['note']['password'] = None
        request['fake']['password'] = token_hex()
        code, _ = create(request)
        self.assertEqual(code, status.HTTP_400_BAD_REQUEST)


class NoteKeyTestCase(TestCase):
    @staticmethod
    def read(slug: str) -> Tuple[int, Dict]:
        client = APIClient()
        response: JsonResponse = client.get(f'{URL}/notes/{slug}/')
        message = json.loads(response.content)
        content = message['data']['content'] if 200 <= response.status_code <= 299 else None
        return response.status_code, content

    def test_create(self):
        request = generate_note_request()
        code, _ = create(request)
        self.assertEqual(code, status.HTTP_201_CREATED)

    def test_read_real(self):
        request = generate_note_request()
        _, slug = create(request)
        code, content = self.read(slug)
        self.assertEqual(content, request['note']['content'])

    def test_read_real_fake(self):
        request = generate_note_request(fake_content=token_hex())
        _, slug = create(request)
        _, real = self.read(slug)
        _, fake = self.read(slug)
        self.assertEqual(real, request['note']['content'])
        self.assertEqual(fake, request['fake']['content'])

    def test_wrong_slug(self):
        request = generate_note_request()
        _, slug_key = create(request)
        slug, key = slug_key.split('/')
        slug = '0' * len(slug)
        code, _ = self.read(f'{slug}/{key}')
        self.assertEqual(code, status.HTTP_404_NOT_FOUND)

    def test_wrong_key(self):
        request = generate_note_request()
        _, slug_key = create(request)
        slug, key = slug_key.split('/')
        key = '0' * len(slug)
        code, _ = self.read(f'{slug}/{key}')
        self.assertEqual(code, status.HTTP_403_FORBIDDEN)

    def test_read_real_twice(self):
        request = generate_note_request()
        _, slug = create(request)
        first_code, _ = self.read(slug)
        second_code, _ = self.read(slug)
        self.assertEqual(first_code, status.HTTP_200_OK)
        self.assertEqual(second_code, status.HTTP_404_NOT_FOUND)

    def test_read_triple(self):
        request = generate_note_request(fake_content=token_hex())
        _, slug = create(request)
        first_code, _ = self.read(slug)
        second_code, _ = self.read(slug)
        third_code, _ = self.read(slug)
        self.assertEqual(first_code, status.HTTP_200_OK)
        self.assertEqual(second_code, status.HTTP_200_OK)
        self.assertEqual(third_code, status.HTTP_404_NOT_FOUND)


class NoteWithPasswordTestCase(TestCase):
    @staticmethod
    def read(slug: str, password: str) -> Tuple[int, str]:
        client = APIClient()
        data = {'password': password}
        response: JsonResponse = client.post(f'{URL}/notes/{slug}/', data, format='json')
        message = json.loads(response.content)
        content = message['data']['content'] if 200 <= response.status_code <= 299 else None
        return response.status_code, content

    def test_read_real(self):
        password = token_hex()
        request = generate_note_request(real_password=password)
        _, slug = create(request)
        code, content = self.read(slug, password)
        self.assertEqual(content, request['note']['content'])

    def test_read_real_fake(self):
        password = token_hex()
        request = generate_note_request(
            real_password=password,
            fake_content=token_hex(),
            fake_password=password
        )
        _, slug = create(request)
        code, real = self.read(slug, password)
        code, fake = self.read(slug, password)
        self.assertEqual(real, request['note']['content'])
        self.assertEqual(fake, request['fake']['content'])

    def test_read_only_real(self):
        real_password = token_hex()
        fake_password = token_hex()
        request = generate_note_request(
            real_password=real_password,
            fake_content=token_hex(),
            fake_password=fake_password
        )
        _, slug = create(request)
        first_code, real = self.read(slug, real_password)
        second_code, _ = self.read(slug, fake_password)
        self.assertEqual(real, request['note']['content'])
        self.assertEqual(second_code, status.HTTP_404_NOT_FOUND)

    def test_read_only_fake(self):
        real_password = token_hex()
        fake_password = token_hex()
        request = generate_note_request(
            real_password=real_password,
            fake_content=token_hex(),
            fake_password=fake_password
        )
        _, slug = create(request)
        first_code, fake = self.read(slug, fake_password)
        second_code, _ = self.read(slug, real_password)
        self.assertEqual(fake, request['fake']['content'])
        self.assertEqual(second_code, status.HTTP_404_NOT_FOUND)

    def test_wrong_slug(self):
        password = token_hex()
        request = generate_note_request()
        code, slug = create(request)
        code, _ = self.read('0' * len(slug), password)
        self.assertEqual(code, status.HTTP_404_NOT_FOUND)

    def test_wrong_password(self):
        password = token_hex()
        request = generate_note_request(real_password=password)
        code, slug = create(request)
        code, _ = self.read(slug, '0' * len(password))
        self.assertEqual(code, status.HTTP_403_FORBIDDEN)
