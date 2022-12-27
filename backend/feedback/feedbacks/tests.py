from secrets import token_hex
from unittest import TestCase

from django.http import JsonResponse
from rest_framework import status
from rest_framework.test import APIClient

URL = '/feedback/api'


class FeedbackCreateTestCase(TestCase):
    def test_create(self):
        client = APIClient()
        data = {
            'feedback': token_hex(),
            'user': 'admin@mail.com'
        }
        response: JsonResponse = client.post(f'{URL}/feedbacks/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
