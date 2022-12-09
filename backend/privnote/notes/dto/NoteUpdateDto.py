from dataclasses import dataclass
from typing import Optional

from privnote.dto.Serializable import Serializable


@dataclass
class NoteUpdateDto(Serializable):
    id: int
    real_content: Optional[str]
    fake_content: Optional[str]

    @staticmethod
    def as_dto(note):
        return NoteUpdateDto(
            id=note.id,
            real_content=note.real_content,
            fake_content=note.fake_content
        )

    def apply(self, note):
        note.real_content = self.real_content
        note.fake_content = self.fake_content
        return note
