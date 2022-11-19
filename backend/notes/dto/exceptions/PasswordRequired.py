from rest_framework import status

from privbird.dto.exceptions.ApiException import ApiException


class PasswordRequiredException(ApiException):
    def __init__(self):
        self.message = 'This note has a password.' \
                       'Enter it to view the information.'
        self.status = status.HTTP_403_FORBIDDEN
        super().__init__()
