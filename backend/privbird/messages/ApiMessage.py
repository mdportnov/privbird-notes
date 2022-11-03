from typing import Any

from privbird.messages.Message import Message
from privbird.messages.Serializable import Serializable


class ApiMessage(Serializable):
    message: Message
    data: Any

    def __init__(self, data: Any = None):
        self.data = data
