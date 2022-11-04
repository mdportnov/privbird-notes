from typing import Any

from drf_yasg.openapi import Schema, TYPE_STRING

from privbird.messages.ApiMessage import ApiMessage
from privbird.messages.Message import Message


class NoteRetrievedMessage(ApiMessage):
    def __init__(self, content: str):
        self.data = {'content': content}
        self.message = Message(
            ru='Заметка успешно получена.',
            en='The note was successfully received.'
        )

    @classmethod
    def api_schema(cls) -> Schema:
        schema = super().api_schema()
        schema.properties['data'].properties = {
            'content': Schema(type=TYPE_STRING)
        }
        return schema
