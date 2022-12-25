from django.utils.translation import gettext_lazy as _
from rest_framework import status

from privnote.dto.exceptions.ApiException import ApiException


class ExternalServerException(ApiException):
    def __init__(self):
        self.message = _('External server does not respond')
        self.status = status.HTTP_500_INTERNAL_SERVER_ERROR
        super().__init__()
