from drf_yasg.openapi import Schema, TYPE_OBJECT, TYPE_STRING

from privbird.dto.messages.ApiMessage import ApiMessage
from privbird.dto.messages.Message import Message


class NoteRetrievedMessage(ApiMessage):
    data_schema = Schema(
        title='Dict',
        type=TYPE_OBJECT,
        properties={'content': Schema(type=TYPE_STRING)}
    )

    def __init__(self, content: str):
        self.data = {'content': content}
        self.message = Message(
            ru='Заметка успешно получена.',
            en='The note was successfully received.'
        )
        super().__init__()
