from rest_framework import status

from privbird.dto.exceptions.ApiException import ApiException


class NoteNotFoundException(ApiException):
    def __init__(self):
        self.message = 'Could not find a note.'
        self.status = status.HTTP_404_NOT_FOUND
        super().__init__()
