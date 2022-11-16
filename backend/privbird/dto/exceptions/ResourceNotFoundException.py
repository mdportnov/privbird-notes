from rest_framework import status

from privbird.dto.exceptions.ApiException import ApiException
from privbird.dto.messages.Message import Message


class ResourceNotFoundException(ApiException):
    def __init__(self):
        self.status = status.HTTP_404_NOT_FOUND
        self.message = Message(
            ru='Запрашиваемый ресурс не найден.',
            en='The requested resource was not found.'
        )
        super().__init__()
