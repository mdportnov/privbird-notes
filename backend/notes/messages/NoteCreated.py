from typing import Any

from privbird.messages.ApiMessage import ApiMessage
from privbird.messages.Message import Message


class NoteCreatedMessage(ApiMessage):
    def __init__(self, data: Any):
        self.data = data
        self.message = Message(
            ru='Заметка успешно создана',
            en='The note was successfully created'
        )
