from privbird.messages.ApiMessage import ApiMessage
from privbird.messages.Message import Message


class FeedbackCreatedMessage(ApiMessage):
    def __init__(self):
        self.message = Message(
            ru='Обращение успешно отправлено',
            en='The feedback was successfully sent'
        )
        super().__init__()
