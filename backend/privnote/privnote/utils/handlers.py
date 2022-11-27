import traceback

from django.http import JsonResponse
from rest_framework.exceptions import APIException, ValidationError, Throttled

from privnote.dto.exceptions.ApiException import ApiException
from privnote.dto.exceptions.ParseException import ParseException
from privnote.dto.exceptions.RateLimitException import RateLimitException
from privnote.dto.exceptions.ResourceNotFoundException import ResourceNotFoundException
from privnote.dto.exceptions.UnexpectedException import UnexpectedException
from privnote.dto.exceptions.ValidationException import ValidationException


def exception_handler(exception, context) -> JsonResponse:
    traceback.print_exc()
    if isinstance(exception, ApiException):
        exception: ApiException
        return exception.as_json_response()
    if isinstance(exception, ValidationError):
        return ValidationException(exception).as_json_response()
    if isinstance(exception, Throttled):
        return RateLimitException().as_json_response()
    if isinstance(exception, APIException):
        return ParseException().as_json_response()
    return UnexpectedException().as_json_response()


def handler404(request, exception) -> JsonResponse:
    return ResourceNotFoundException().as_json_response()


def handler500(request) -> JsonResponse:
    return UnexpectedException().as_json_response()
