from rest_framework import status

from feedback.dto.exceptions.ApiException import ApiException


class ResourceNotFoundException(ApiException):
    def __init__(self):
        self.message = 'The requested resource was not found.'
        self.status = status.HTTP_404_NOT_FOUND
        super().__init__()
