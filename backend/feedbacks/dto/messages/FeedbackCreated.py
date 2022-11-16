from rest_framework import status

from privbird.dto.messages.ApiMessage import ApiMessage
from privbird.dto.messages.Message import Message


class FeedbackCreatedMessage(ApiMessage):
    def __init__(self):
        self.status = status.HTTP_201_CREATED
        self.message = Message(
            ru='Обращение успешно отправлено.',
            en='The feedback was successfully sent.'
        )
        super().__init__()
