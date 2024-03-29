from dataclasses import dataclass
from typing import Optional

from privnote.dto.Serializable import Serializable


@dataclass
class NotePartRequest(Serializable):
    content: Optional[str]
    password: Optional[str]
    notification: Optional[bool]
