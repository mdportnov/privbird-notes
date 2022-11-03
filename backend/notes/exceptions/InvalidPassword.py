from rest_framework import status

from privbird.exceptions.shared.ApiException import ApiException
from privbird.messages.Message import Message


class InvalidPasswordException(ApiException):
    def __init__(self):
        self.status_code: int = status.HTTP_403_FORBIDDEN
        self.message: Message = Message(
            ru='Вы ввели неправильный пароль. Попробуйте снова',
            en='You have entered the wrong password. Try again'
        )
