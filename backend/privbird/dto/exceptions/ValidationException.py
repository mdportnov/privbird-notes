from rest_framework import status
from rest_framework.exceptions import ValidationError

from privbird.dto.exceptions.ApiException import ApiException


class ValidationException(ApiException):
    def __init__(self, error: ValidationError):
        self.message = 'Invalid data.'
        self.error = error
        self.status = status.HTTP_400_BAD_REQUEST
        super().__init__()
