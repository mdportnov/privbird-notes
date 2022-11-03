from dataclasses import dataclass


@dataclass
class NoteRequest:
    content: str
    password: str
    notification: bool
