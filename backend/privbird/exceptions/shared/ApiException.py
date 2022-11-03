from abc import ABC

from django.core.exceptions import FieldError
from django.utils.timezone import now
from rest_framework.exceptions import APIException


class ApiException(ABC, APIException):
    ru: str
    en: str
    errors = FieldError()
    timestamp = now()
