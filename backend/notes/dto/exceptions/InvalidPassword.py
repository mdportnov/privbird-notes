from rest_framework import status

from privbird.dto.exceptions.ApiException import ApiException
from privbird.dto.messages.Message import Message


class InvalidPasswordException(ApiException):
    def __init__(self):
        self.status = status.HTTP_403_FORBIDDEN
        self.message: Message = Message(
            ru='Вы ввели неправильный пароль. Попробуйте снова.',
            en='You have entered the wrong password. Try again.'
        )
        super().__init__()
