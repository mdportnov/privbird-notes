from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import exception_handler

from privbird.exceptions.ExceptionSerializer import ExceptionSerializer
from privbird.exceptions.shared.ApiException import ApiException
from privbird.exceptions.shared.ValidationException import ValidationException


def handler(exc, context):
    if issubclass(type(exc), ValidationError):
        exc = ValidationException(error=exc)
    if issubclass(type(exc), ApiException):
        response = Response()
        exc: ApiException
        response.status_code = exc.status_code
        response.data = ExceptionSerializer(exc).data
        return response
    return exception_handler(exc, context)
