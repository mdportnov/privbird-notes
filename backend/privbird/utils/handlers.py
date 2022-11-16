import traceback

from django.http import JsonResponse
from rest_framework.exceptions import ValidationError

from privbird.dto.exceptions.ApiException import ApiException
from privbird.dto.exceptions.ParseException import ParseException
from privbird.dto.exceptions.ResourceNotFoundException import ResourceNotFoundException
from privbird.dto.exceptions.UnexpectedException import UnexpectedException
from privbird.dto.exceptions.ValidationException import ValidationException


def exception_handler(exception, context) -> JsonResponse:
    # raise exception
    traceback.print_exc()
    if isinstance(exception, ApiException):
        exception: ApiException
        return exception.as_json_response()
    if isinstance(exception, ValidationError):
        return ValidationException(exception.detail).as_json_response()
    if isinstance(exception, ParseException):
        return ParseException().as_json_response()
    return UnexpectedException().as_json_response()


def handler404(request, exception) -> JsonResponse:
    return ResourceNotFoundException().as_json_response()


def handler500(request) -> JsonResponse:
    return UnexpectedException().as_json_response()
