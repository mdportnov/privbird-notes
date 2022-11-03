from abc import ABC


class ApiMessage(ABC):
    ru: str
    en: str
    data: str

    def __init__(self, data: str = None):
        self.data = data
