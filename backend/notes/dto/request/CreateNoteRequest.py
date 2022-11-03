from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

from notes.dto.request.CreateFlateNoteRequest import CreateFlateNoteRequest
from notes.dto.request.NoteOptionsRequest import NoteOptionsRequest
from notes.dto.request.NoteRequest import NoteRequest


@dataclass
class CreateNoteRequest:
    note: NoteRequest
    fake: NoteRequest
    options: NoteOptionsRequest

    @staticmethod
    def from_dict(**kwargs) -> CreateNoteRequest:
        data = CreateNoteRequest(**kwargs)
        data.note = NoteRequest(**data.note)
        data.fake = NoteRequest(**data.fake)
        data.options = NoteOptionsRequest(**data.options)
        return data

    def enflate_dict(self) -> Dict:
        return {
            "content": self.note.content,
            "password": self.note.password,
            "notification": self.note.notification,

            "fakeContent": self.fake.content,
            "fakePassword": self.fake.password,
            "fakeNotification": self.fake.notification,

            "network": self.options.network,
            "expires": self.options.expires,
            "email": self.options.email
        }
