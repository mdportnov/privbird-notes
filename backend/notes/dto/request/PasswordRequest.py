from dataclasses import dataclass

from privbird.dto.Serializable import Serializable


@dataclass
class PasswordRequest(Serializable):
    password: str
