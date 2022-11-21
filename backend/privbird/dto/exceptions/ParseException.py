from rest_framework import status

from privbird.dto.exceptions.ApiException import ApiException


class ParseException(ApiException):
    def __init__(self):
        self.message = 'Invalid data.'
        self.status = status.HTTP_400_BAD_REQUEST
        super().__init__()
