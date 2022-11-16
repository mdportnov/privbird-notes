from rest_framework import status

from privbird.dto.exceptions.ApiException import ApiException
from privbird.dto.messages.Message import Message


class PasswordRequiredException(ApiException):
    def __init__(self):
        self.status = status.HTTP_403_FORBIDDEN
        self.message = Message(
            ru='У этой заметки есть пароль.\nВведите его, чтобы просмотреть информацию.',
            en='This note has a password.\nEnter it to view the information.'
        )
        super().__init__()
