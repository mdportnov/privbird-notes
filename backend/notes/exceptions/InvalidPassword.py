from rest_framework import status

from privbird.messages.ApiException import ApiException
from privbird.messages.Message import Message


class InvalidPasswordException(ApiException):
    def __init__(self):
        self.detail = 'Invalid password'
        self.status_code: int = status.HTTP_403_FORBIDDEN
        self.message: Message = Message(
            ru='Ты ввел неправильный пароль. Пробуй снова',
            en='You have entered the wrong password. Try again'
        )
