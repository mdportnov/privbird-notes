from drf_yasg.openapi import Schema, TYPE_OBJECT, TYPE_STRING
from rest_framework import status

from privbird.dto.messages.ApiMessage import ApiMessage
from privbird.dto.messages.Message import Message


class NoteCreatedMessage(ApiMessage):
    data_schema = Schema(
        title='Dict',
        type=TYPE_OBJECT,
        properties={'slug': Schema(type=TYPE_STRING)}
    )

    def __init__(self, slug: str):
        self.data = {'slug': slug}
        self.status = status.HTTP_201_CREATED
        self.message = Message(
            ru='Заметка успешно создана.\nЗаметка будет уничтожена после прочтения!\nНе забудьте скопировать ссылку!',
            en='The note has been successfully created.\nThe note will be destroyed after reading it!\nDon’t forget '
               'to copy the link!'
        )
        super().__init__()
