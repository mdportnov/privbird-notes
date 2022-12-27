from dataclasses import dataclass

from privnote.dto.Serializable import Serializable


@dataclass
class PasswordRequest(Serializable):
    password: str
