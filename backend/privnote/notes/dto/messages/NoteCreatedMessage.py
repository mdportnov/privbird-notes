from dataclasses import dataclass
from typing import Dict

from drf_yasg.openapi import Schema, TYPE_OBJECT, TYPE_STRING
from rest_framework import status

from privnote.dto.messages.ApiMessage import ApiMessage


@dataclass
class NoteCreatedMessage(ApiMessage):
    data: Dict

    def __init__(self, slug: str):
        self.message = 'The note has been successfully created.' \
                       'The note will be destroyed after reading it!' \
                       'Don’t forget to copy the link!'
        self.data = {'slug': slug}
        self.status = status.HTTP_201_CREATED
        super().__init__()

    @classmethod
    def api_schema(cls) -> Schema:
        schema = super().api_schema()
        schema.properties['data'] = Schema(
            title='Dict',
            type=TYPE_OBJECT,
            properties={'slug': Schema(type=TYPE_STRING)}
        )
        return schema
