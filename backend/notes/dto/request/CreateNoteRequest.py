from dataclasses import dataclass

from notes.dto.request.NoteRequest import NoteRequest
from notes.dto.request.OptionsRequest import OptionsRequest
from notes.models import Note
from privbird.dto.Serializable import Serializable


@dataclass
class CreateNoteRequest(Serializable):
    note: NoteRequest
    fake: NoteRequest
    options: OptionsRequest

    def validate_and_save(self) -> Note:
        note = Note(
            real_content=self.note.content,
            real_password=self.note.password,
            real_notification=self.note.notification,

            fake_content=self.fake.content,
            fake_password=self.fake.password,
            fake_notification=self.fake.notification,

            network=self.options.network,
            expires=self.options.expires.get_expiration(),
            email=self.options.email
        )
        note.validate()
        note.save()
        return note
