from typing import Dict, Tuple

from django.http import JsonResponse
from rest_framework.exceptions import ValidationError

from privbird.exceptions.shared.ApiException import ApiException
from privbird.exceptions.shared.UnexpectedException import UnexpectedException
from privbird.exceptions.shared.ValidationException import ValidationException


def common_handler(exception: ApiException) -> tuple[int, Dict]:
    return exception.status_code, exception.serialize()


def validation_error_handler(error: ValidationError) -> Tuple[int, Dict]:
    exception = ValidationException(error.detail)
    return common_handler(exception)


def unexpected_handler() -> Tuple[int, Dict]:
    exception = UnexpectedException()
    return common_handler(exception)


def prepare_response(exception, exc_handler) -> JsonResponse:
    code, data = exc_handler(exception)
    response = JsonResponse(data=data)
    response.status_code = code
    return response


def handler(exception, context) -> JsonResponse:
    exception_handler = unexpected_handler
    if issubclass(type(exception), ValidationError):
        exception_handler = validation_error_handler
    if issubclass(type(exception), ApiException):
        exception_handler = common_handler
    return prepare_response(exception, exception_handler)
