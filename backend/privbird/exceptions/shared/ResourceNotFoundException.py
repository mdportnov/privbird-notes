from rest_framework import status

from privbird.exceptions.shared.ApiException import ApiException
from privbird.messages.Message import Message


class ResourceNotFoundException(ApiException):
    def __init__(self):
        self.status_code = status.HTTP_404_NOT_FOUND
        self.message = Message(
            ru='Запрашиваемый ресурс не найден.',
            en='The requested resource was not found.'
        )
