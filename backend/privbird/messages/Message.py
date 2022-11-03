from dataclasses import dataclass

from privbird.messages.Serializable import Serializable


@dataclass
class Message(Serializable):
    ru: str
    en: str
