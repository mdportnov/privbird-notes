from rest_framework import status

from privbird.exceptions.shared.ApiException import ApiException
from privbird.messages.Message import Message


class PasswordRequiredException(ApiException):
    def __init__(self):
        self.status_code = status.HTTP_403_FORBIDDEN
        self.message = Message(
            ru='Эта заметка защищена паролем. Тебе нужно ввести его, чтобы просмотреть информацию',
            en='This note has a password. You must enter it to view the information'
        )
