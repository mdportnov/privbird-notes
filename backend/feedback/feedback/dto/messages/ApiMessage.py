from dataclasses import dataclass

from drf_yasg.openapi import Schema, TYPE_OBJECT, TYPE_STRING

from feedback.dto.ApiResponse import ApiResponse


@dataclass
class ApiMessage(ApiResponse):
    """
    Data transfer object for messages sent by API to the client
    """

    def __init__(self):
        super().__init__()

    @classmethod
    def api_schema(cls) -> Schema:
        return Schema(
            title=cls.__name__,
            type=TYPE_OBJECT,
            properties={
                'message': Schema(title='text', type=TYPE_STRING)
            }
        )
