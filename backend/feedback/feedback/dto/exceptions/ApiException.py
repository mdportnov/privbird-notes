from dataclasses import dataclass
from typing import Optional

from rest_framework.exceptions import APIException

from feedback.dto.ApiResponse import ApiResponse


@dataclass
class ApiException(APIException, ApiResponse):
    """
    Data transfer object for error messages sent by API to the client
    """

    def __init__(self, message: Optional[str] = None):
        if message:
            self.message = message
        APIException.__init__(self)
        ApiResponse.__init__(self)
