from dataclasses import dataclass

from notes.models import Note
from notes.utils.expiration import Expiration


@dataclass
class NoteOptionsRequest:
    network: Note.Network
    expires: Expiration
    email: str
