from dataclasses import dataclass
from typing import Dict

from rest_framework import status
from rest_framework.exceptions import ValidationError

from privnote.dto.exceptions.ApiException import ApiException


@dataclass
class ValidationException(ApiException):
    error: Dict

    def __init__(self, error: ValidationError):
        self.message = 'Invalid data.'
        self.error = {key: error.detail[key] for key in error.detail.keys()}
        self.status = status.HTTP_400_BAD_REQUEST
        super().__init__()
