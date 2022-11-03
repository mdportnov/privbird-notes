from dataclasses import dataclass

from privbird.utils.Serializable import Serializable


@dataclass
class PasswordRequest(Serializable):
    password: str
