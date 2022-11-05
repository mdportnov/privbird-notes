from drf_yasg.openapi import Schema, TYPE_STRING

from privbird.messages.ApiMessage import ApiMessage
from privbird.messages.Message import Message


class NoteCreatedMessage(ApiMessage):
    def __init__(self, slug: str):
        self.data = {'slug': slug}
        self.message = Message(
            ru='Заметка успешно создана.\nЗаметка будет уничтожена после прочтения!\nНе забудьте скопировать ссылку!',
            en='The note has been successfully created.\nThe note will be destroyed after reading it!\nDon’t forget '
               'to copy the link!'
        )

    @classmethod
    def api_schema(cls) -> Schema:
        schema = super().api_schema()
        schema.properties['data'].properties = {
            'slug': Schema(type=TYPE_STRING)
        }
        return schema
