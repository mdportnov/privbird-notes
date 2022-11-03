from rest_framework import status
from rest_framework.exceptions import ValidationError

from privbird.messages.ApiException import ApiException
from privbird.messages.Message import Message


class ValidationException(ApiException):
    def __init__(self, error: ValidationError):
        self.error = error
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = 'Invalid data'
        self.message = Message(
            ru="Некорректные данные",
            en="Invalid data"
        )
