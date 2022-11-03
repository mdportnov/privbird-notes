from django.core.exceptions import ValidationError
from django.utils.datetime_safe import datetime
from django.utils.timezone import now
from rest_framework.exceptions import APIException

from privbird.messages import Message
from privbird.messages.Serializable import Serializable


class ApiException(APIException, Serializable):
    message: Message
    status_code: int
    timestamp: datetime = now()
    error: ValidationError = None

    def __init__(self):
        delattr(ApiException, 'detail')
