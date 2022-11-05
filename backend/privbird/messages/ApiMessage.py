from typing import Any, Optional

from drf_yasg.openapi import Schema, TYPE_OBJECT

from privbird.messages.Message import Message
from privbird.utils.Serializable import Serializable


class ApiMessage(Serializable):
    """
    Data transfer object for messages sent by API to the client
    """

    message: Message

    data: Optional[Any]

    def __init__(self, data: Any = None):
        self.data = data

    @classmethod
    def api_schema(cls) -> Schema:
        return Schema(
            title=cls.__name__,
            type=TYPE_OBJECT,
            properties={
                'message': Message.api_schema(),
                'data': Schema(
                    title='Any',
                    type=TYPE_OBJECT
                )
            }
        )
