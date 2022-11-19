from rest_framework import status

from privbird.dto.exceptions.ApiException import ApiException


class InvalidPasswordException(ApiException):
    def __init__(self):
        self.message = 'You have entered the wrong password. Try again.'
        self.status = status.HTTP_403_FORBIDDEN
        super().__init__()
