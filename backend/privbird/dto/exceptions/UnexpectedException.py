from rest_framework import status

from privbird.dto.exceptions.ApiException import ApiException
from privbird.dto.messages.Message import Message


class UnexpectedException(ApiException):
    def __init__(self):
        self.status = status.HTTP_500_INTERNAL_SERVER_ERROR
        self.message = Message(
            ru='Произошла ошибка.\nПопробуйте еще раз или обратитесь в службу поддержки!',
            en='There was an error.\nTry again or contact support!'
        )
        super().__init__()
