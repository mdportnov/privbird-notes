from rest_framework import status
from rest_framework.exceptions import ValidationError

from privbird.exceptions.shared.ApiException import ApiException
from privbird.messages.Message import Message


class UnexpectedException(ApiException):
    def __init__(self):
        self.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        self.message = Message(
            ru='Произошла ошибка.\nПопробуйте еще раз или обратитесь в службу поддержки!',
            en='There was an error.\nTry again or contact support!'
        )
