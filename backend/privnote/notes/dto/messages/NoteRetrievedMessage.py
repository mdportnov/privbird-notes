from dataclasses import dataclass
from typing import Dict

from drf_yasg.openapi import Schema, TYPE_OBJECT, TYPE_STRING

from privnote.dto.messages.ApiMessage import ApiMessage


@dataclass
class NoteRetrievedMessage(ApiMessage):
    data: Dict

    def __init__(self, content: str):
        self.message = 'The note was successfully received.'
        self.data = {'content': content}
        super().__init__()

    @classmethod
    def api_schema(cls) -> Schema:
        schema = super().api_schema()
        schema.properties['data'] = Schema(
            title='Dict',
            type=TYPE_OBJECT,
            properties={'content': Schema(type=TYPE_STRING)}
        )
        return schema
