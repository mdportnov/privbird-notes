from abc import ABC
from dataclasses import dataclass
from typing import Tuple

from django.http import JsonResponse
from django.utils.datetime_safe import datetime
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from rest_framework import status

from privnote.dto.Serializable import Serializable


@dataclass(kw_only=True)
class ApiResponse(Serializable, ABC):
    """
    Abstract data transfer object for responses
    """

    message: str
    status: int = status.HTTP_200_OK
    timestamp: datetime = now()
    exclude: Tuple[str] = ('exclude', 'status')

    def __init__(self):
        self.message = _(self.message)

    def as_json_response(self) -> JsonResponse:
        response = JsonResponse(data=self.serialize())
        response.status_code = self.status
        return response
