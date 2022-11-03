from typing import Any

from privbird.messages.ApiMessage import ApiMessage
from privbird.messages.Message import Message


class NoteCreatedMessage(ApiMessage):
    def __init__(self, data: Any):
        self.data = data
        self.message = Message(
            ru='Заметка успешно создана.\nЗаметка будет уничтожена после прочтения!\nНе забудьте скопировать ссылку!',
            en='The note has been successfully created.\nThe note will be destroyed after reading it!\nDon’t forget '
               'to copy the link! '
        )
