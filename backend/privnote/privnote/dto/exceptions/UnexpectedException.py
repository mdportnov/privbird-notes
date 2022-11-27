from rest_framework import status

from privnote.dto.exceptions.ApiException import ApiException


class UnexpectedException(ApiException):
    def __init__(self):
        self.message = 'There was an error.' \
                       'Try again or contact support!'
        self.status = status.HTTP_500_INTERNAL_SERVER_ERROR
        super().__init__()
