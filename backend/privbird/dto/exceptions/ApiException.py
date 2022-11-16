from dataclasses import dataclass
from typing import Optional

from django.core.exceptions import ValidationError
from rest_framework.exceptions import APIException

from privbird.dto.ApiResponse import ApiResponse


@dataclass
class ApiException(APIException, ApiResponse):
    """
    Data transfer object for error messages sent by API to the client
    """

    error: Optional[ValidationError] = None

    def __init__(self):
        super().__init__()
