from dataclasses import dataclass

from rest_framework import serializers

from notes.dto.request.NoteOptionsRequest import NoteOptionsRequest
from notes.dto.request.NoteRequest import NoteRequest
from notes.models import Note
from privbird.utils.Serializable import Serializable


@dataclass
class CreateNoteRequest(Serializable):
    note: NoteRequest
    fake: NoteRequest
    options: NoteOptionsRequest

    def validate(self):
        if self.note.content is None:
            raise serializers.ValidationError({'note': {'content': 'This field may not be null.'}})

        if self.note.notification is None:
            raise serializers.ValidationError({'note': {'content': 'This field may not be null.'}})

        if self.fake.content is None:
            if self.fake.password is not None:
                raise serializers.ValidationError({'fake': {'password': 'This field must be null.'}})

            if self.fake.notification is not None:
                raise serializers.ValidationError({'fake': {'notification': 'This field must be null.'}})

        if self.fake.content is not None:
            if self.fake.notification is None:
                raise serializers.ValidationError({'fake': {'notification': 'This field may not be null.'}})

        if self.options.email is None:
            if self.note.notification or self.fake.notification:
                raise serializers.ValidationError({'options': {'email': 'This field may not be null.'}})

    def save_as_note(self) -> Note:
        note = Note(
            content=self.note.content,
            password=self.note.password,
            notification=self.note.notification,

            fakeContent=self.fake.content,
            fakePassword=self.fake.password,
            fakeNotification=self.fake.notification,

            network=self.options.network,
            expires=self.options.expires.get_expiration(),
            email=self.options.email
        )
        note.save()
        return note
