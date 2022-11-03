from dataclasses import dataclass

from notes.models import Note
from notes.utils.expiration import Expiration


@dataclass
class CreateFlateNoteRequest:
    content: str
    password: str
    notification: bool

    fakeContent: str
    fakePassword: str
    fakeNotification: bool

    network: Note.Network
    expires: Expiration
    email: str
