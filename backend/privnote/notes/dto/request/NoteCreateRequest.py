from __future__ import annotations

from dataclasses import dataclass

from notes.dto.request.NoteOptionsRequest import NoteOptionsRequest
from notes.dto.request.NotePartRequest import NotePartRequest
from privnote.dto.Serializable import Serializable


@dataclass
class NoteCreateRequest(Serializable):
    note: NotePartRequest
    fake: NotePartRequest
    options: NoteOptionsRequest

    def as_note(self):
        from notes.models import Note
        return Note(
            real_content=self.note.content,
            real_password=self.note.password,
            real_notification=self.note.notification,

            fake_content=self.fake.content,
            fake_password=self.fake.password,
            fake_notification=self.fake.notification,

            expires=self.options.expires.get_expiration(),
            email=self.options.email
        )

    def save(self) -> str:
        from notes.tasks import call_task, note_save
        return call_task(note_save, request=self.serialize())
