from drf_yasg.openapi import Schema, TYPE_NUMBER, TYPE_OBJECT, TYPE_STRING
from rest_framework import status

from privbird.dto.exceptions.ApiException import ApiException


class PasswordRequiredException(ApiException):
    def __init__(self):
        self.message = 'This note has a password.' \
                       'Enter it to view the information.'
        self.status = status.HTTP_403_FORBIDDEN
        super().__init__()

    @classmethod
    def api_schema(cls) -> Schema:
        return Schema(
            title=cls.__name__,
            type=TYPE_OBJECT,
            properties={
                'message': Schema(title='text', type=TYPE_STRING),
                'status': Schema(title='status', type=TYPE_NUMBER)
            }
        )
