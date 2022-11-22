from dataclasses import dataclass

from rest_framework.exceptions import APIException

from privbird.dto.ApiResponse import ApiResponse


@dataclass
class ApiException(APIException, ApiResponse):
    """
    Data transfer object for error messages sent by API to the client
    """

    def __init__(self):
        APIException.__init__(self)
        ApiResponse.__init__(self)
