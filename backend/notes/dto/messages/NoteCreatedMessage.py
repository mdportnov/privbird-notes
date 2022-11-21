from drf_yasg.openapi import Schema, TYPE_OBJECT, TYPE_STRING
from rest_framework import status

from privbird.dto.messages.ApiMessage import ApiMessage


class NoteCreatedMessage(ApiMessage):
    data_schema = Schema(
        title='Dict',
        type=TYPE_OBJECT,
        properties={'slug': Schema(type=TYPE_STRING)}
    )

    def __init__(self, slug: str):
        self.message = 'The note has been successfully created.' \
                       'The note will be destroyed after reading it!' \
                       'Don’t forget to copy the link!'
        self.data = {'slug': slug}
        self.status = status.HTTP_201_CREATED
        super().__init__()
