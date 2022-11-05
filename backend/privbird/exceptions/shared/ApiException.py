from django.core.exceptions import ValidationError
from rest_framework.exceptions import APIException

from privbird.messages import Message
from privbird.utils.Serializable import Serializable


class ApiException(APIException, Serializable):
    message: Message
    status_code: int
    error: ValidationError = None
    detail: str = None

    def __init__(self):
        delattr(ApiException, 'detail')
