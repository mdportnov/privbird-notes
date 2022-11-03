import json

from rest_framework.exceptions import ValidationError

from privbird.exceptions.shared.ApiException import ApiException


class ValidationException(ApiException):

    def __init__(self, error: ValidationError):
        self.ru = 'Некорректные данные'
        self.en = 'Invalid data'
        self.status_code = error.status_code
        self.errors = json.dumps(error.detail)
