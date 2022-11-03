from typing import Dict, Tuple

from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import exception_handler

from privbird.exceptions.shared.ValidationException import ValidationException
from privbird.exceptions.shared.ApiException import ApiException


def validation_error_handler(error: ValidationError) -> Tuple[int, Dict]:
    exception = ValidationException(error.detail)
    return exception.status_code, exception.serialize()


def common_handler(exception: ApiException) -> tuple[int, Dict]:
    return exception.status_code, exception.serialize()


def prepare_response(exception, exc_handler) -> Response:
    code, data = exc_handler(exception)
    response = Response()
    response.status_code = code
    response.data = data
    return response


def handler(exception, context) -> Response:
    if issubclass(type(exception), ValidationError):
        return prepare_response(exception, validation_error_handler)
    if issubclass(type(exception), ApiException):
        return prepare_response(exception, common_handler)
    return exception_handler(exception, context)
