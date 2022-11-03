from dataclasses import dataclass

from django.utils.datetime_safe import datetime

from notes.models import Note


@dataclass
class CreateNoteRequest:
    content: str
    password: str
    notification: bool

    fakeContent: str
    fakePassword: str
    fakeNotification: bool

    network: Note.Network
    expires: datetime
    email: str
