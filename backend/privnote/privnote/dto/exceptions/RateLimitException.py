from django.utils.translation import gettext_lazy as _
from rest_framework import status

from privnote.dto.exceptions.ApiException import ApiException


class RateLimitException(ApiException):
    def __init__(self):
        self.message = _('Request limit reached.')
        self.status = status.HTTP_429_TOO_MANY_REQUESTS
        super().__init__()
