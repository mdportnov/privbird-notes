from rest_framework import status

from privbird.exceptions.shared.ApiException import ApiException
from privbird.messages.Message import Message


class PasswordRequiredException(ApiException):
    def __init__(self):
        self.status_code = status.HTTP_403_FORBIDDEN
        self.message = Message(
            ru='У этой заметки есть пароль.\nВведите его, чтобы просмотреть информацию.',
            en='This note has a password.\nEnter it to view the information.'
        )
