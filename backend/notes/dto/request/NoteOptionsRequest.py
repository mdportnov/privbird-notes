from dataclasses import dataclass
from typing import Optional

from notes.models import Note
from notes.utils.expiration import Expiration
from privbird.utils.Serializable import Serializable


@dataclass
class NoteOptionsRequest(Serializable):
    network: Note.Network
    expires: Expiration
    email: Optional[str]
