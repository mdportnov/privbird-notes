from __future__ import annotations

from dataclasses import dataclass

from notes.dto.request.NoteOptionsRequest import NoteOptionsRequest
from notes.dto.request.NotePartRequest import NotePartRequest
from privnote import settings
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
        from notes.tasks import note_save, call_task
        print(f'Save note with network {self.options.network}')
        return call_task(
            task=note_save,
            queue=settings.CELERY_DEFAULT_QUEUE,
            initial_queue=settings.CELERY_DEFAULT_QUEUE,
            destination_queue=self.options.network.value,
            request=self.serialize()
        )
