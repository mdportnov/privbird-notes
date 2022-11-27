from dataclasses import dataclass
from typing import Optional

from notes.models import Note
from notes.utils.Expires import Expires
from privnote.dto.Serializable import Serializable


@dataclass
class OptionsRequest(Serializable):
    network: Note.Network
    expires: Expires
    email: Optional[str]
