import traceback

from django.http import JsonResponse
from rest_framework.exceptions import APIException, Throttled, ValidationError

from feedback.dto.exceptions.ApiException import ApiException
from feedback.dto.exceptions.ParseException import ParseException
from feedback.dto.exceptions.RateLimitException import RateLimitException
from feedback.dto.exceptions.ResourceNotFoundException import ResourceNotFoundException
from feedback.dto.exceptions.UnexpectedException import UnexpectedException
from feedback.dto.exceptions.ValidationException import ValidationException


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
