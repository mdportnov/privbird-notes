from rest_framework import status

from privnote.dto.exceptions.ApiException import ApiException
from django.utils.translation import gettext_lazy as _


class HostNotSetException(ApiException):
    def __init__(self):
        self.message = _('Host for this network is not set')
        self.status = status.HTTP_500_INTERNAL_SERVER_ERROR
        super().__init__()
