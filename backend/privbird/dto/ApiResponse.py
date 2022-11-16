from abc import ABC
from dataclasses import dataclass
from typing import Tuple

from django.http import JsonResponse
from rest_framework import status

from privbird.dto.Serializable import Serializable
from privbird.dto.messages.Message import Message


@dataclass(kw_only=True)
class ApiResponse(Serializable, ABC):
    """
    Abstract data transfer object for responses
    """

    message: Message
    status: int = status.HTTP_200_OK
    exclude: Tuple[str] = ('exclude', 'status')

    def __init__(self):
        pass

    def as_json_response(self) -> JsonResponse:
        response = JsonResponse(data=self.serialize())
        response.status_code = self.status
        return response
