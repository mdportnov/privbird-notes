from rest_framework import status

from privbird.dto.exceptions.ApiException import ApiException
from privbird.dto.messages.Message import Message


class ParseException(ApiException):
    def __init__(self):
        self.status = status.HTTP_400_BAD_REQUEST
        self.message = Message(
            ru='Некорректные данные.',
            en='Invalid data.'
        )
        super().__init__()
