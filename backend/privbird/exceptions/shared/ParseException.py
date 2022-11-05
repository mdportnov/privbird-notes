from rest_framework import status

from privbird.exceptions.shared.ApiException import ApiException
from privbird.messages.Message import Message


class ParseException(ApiException):
    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.message = Message(
            ru='Некорректные данные',
            en='Invalid data'
        )
