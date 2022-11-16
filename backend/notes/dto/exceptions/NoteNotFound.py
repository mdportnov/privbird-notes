from rest_framework import status

from privbird.dto.exceptions.ApiException import ApiException
from privbird.dto.messages.Message import Message


class NoteNotFoundException(ApiException):
    def __init__(self):
        self.status = status.HTTP_404_NOT_FOUND
        self.message = Message(
            ru='Не удалось найти заметку.',
            en='Could not find a note.'
        )
        super().__init__()
