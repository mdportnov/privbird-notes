from django.http import JsonResponse
from rest_framework.exceptions import ParseError, ValidationError

from privbird.exceptions.shared.ApiException import ApiException
from privbird.exceptions.shared.ParseException import ParseException
from privbird.exceptions.shared.UnexpectedException import UnexpectedException
from privbird.exceptions.shared.ValidationException import ValidationException


def validation_error_handler(error: ValidationError) -> ValidationException:
    return ValidationException(error.detail)


def parse_error_handler(exception) -> ParseException:
    return ParseException()


def unexpected_handler(exception) -> UnexpectedException:
    return UnexpectedException()


def response_exception(exception: ApiException) -> JsonResponse:
    response = JsonResponse(data=exception.serialize())
    response.status_code = exception.status_code
    return response


def handler(exception, context) -> JsonResponse:
    exception_type = type(exception)
    print(exception, context)
    if issubclass(exception_type, ValidationError):
        exception = validation_error_handler(exception)
    elif issubclass(exception_type, ParseError):
        exception = parse_error_handler(exception)
    elif not issubclass(exception_type, ApiException):
        exception = unexpected_handler(exception)
    return response_exception(exception)
