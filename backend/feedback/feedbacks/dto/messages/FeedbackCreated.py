from rest_framework import status

from feedback.dto.messages.ApiMessage import ApiMessage


class FeedbackCreatedMessage(ApiMessage):
    def __init__(self):
        self.message = 'The feedback was successfully sent.'
        self.status = status.HTTP_201_CREATED
        super().__init__()
