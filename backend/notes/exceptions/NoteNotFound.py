from rest_framework import status

from privbird.exceptions.shared.ApiException import ApiException
from privbird.messages.Message import Message


class NoteNotFoundException(ApiException):
    def __init__(self):
        self.status_code = status.HTTP_404_NOT_FOUND
        self.message = Message(
            ru='Не удалось найти заметку.',
            en='Could not find a note.'
        )
