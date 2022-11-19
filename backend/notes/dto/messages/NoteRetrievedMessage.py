from drf_yasg.openapi import Schema, TYPE_OBJECT, TYPE_STRING

from privbird.dto.messages.ApiMessage import ApiMessage


class NoteRetrievedMessage(ApiMessage):
    data_schema = Schema(
        title='Dict',
        type=TYPE_OBJECT,
        properties={'content': Schema(type=TYPE_STRING)}
    )

    def __init__(self, content: str):
        self.message = 'The note was successfully received.'
        self.data = {'content': content}
        super().__init__()
