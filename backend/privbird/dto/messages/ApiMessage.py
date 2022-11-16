from dataclasses import dataclass
from typing import Dict, Optional

from drf_yasg.openapi import Schema, TYPE_OBJECT

from privbird.dto.ApiResponse import ApiResponse
from privbird.dto.messages.Message import Message


@dataclass
class ApiMessage(ApiResponse):
    """
    Data transfer object for messages sent by API to the client
    """

    data: Optional[Dict] = None
    data_schema = Schema(title='Dict', type=TYPE_OBJECT, nullable=True)

    def __init__(self):
        super().__init__()

    @classmethod
    def api_schema(cls) -> Schema:
        return Schema(
            title=cls.__name__,
            type=TYPE_OBJECT,
            properties={
                'message': Message.api_schema(),
                'data': cls.data_schema
            }
        )
