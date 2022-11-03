from dataclasses import dataclass

from privbird.utils.Serializable import Serializable


@dataclass
class Message(Serializable):
    ru: str
    en: str
