from __future__ import annotations

import secrets

from django.contrib.auth.hashers import check_password, make_password
from django.db import models

from notes.exceptions.InvalidPassword import InvalidPasswordException
from notes.exceptions.NoteNotFound import NoteNotFoundException
from notes.exceptions.PasswordRequired import PasswordRequiredException
from notes.utils.constants import Constants
from notes.utils.crypto import decrypt, encrypt
from notes.utils.expiration import Expiration
from notes.utils.slug import generate_slug


class Note(models.Model):
    class Network(models.TextChoices):
        HTTPS = 'HTTPS'
        TOR = 'TOR'
        I2P = 'I2P'

        @classmethod
        def max_length(cls) -> int:
            return max(map(len, cls.values))

    content = models.TextField(max_length=Constants.MAX_CONTENT_LENGTH, null=True)
    password = models.CharField(max_length=Constants.MAX_PASSWORD_LENGTH, default=None, null=True)
    notification = models.BooleanField(default=False)

    fake_content = models.TextField(max_length=Constants.MAX_CONTENT_LENGTH, default=None, null=True)
    fake_password = models.TextField(max_length=Constants.MAX_PASSWORD_LENGTH, default=None, null=True)
    fake_notification = models.BooleanField(default=None, null=True)

    salt = models.CharField(max_length=Constants.SALT_LENGTH, default=None, null=True)
    slug = models.SlugField(max_length=Constants.SLUG_LENGTH, unique=True)
    network = models.CharField(max_length=5, choices=Network.choices, default=Network.HTTPS)
    expires = models.DateTimeField(default=Expiration.YEAR.get_expiration())
    email = models.EmailField(default=None, null=True)

    @staticmethod
    def __find_by_slug(slug: str) -> Note:
        if not Note.objects.filter(slug=slug).exists():
            raise NoteNotFoundException()
        return Note.objects.get(slug=slug)

    @staticmethod
    def find_by_slug(slug: str) -> str:
        note = Note.__find_by_slug(slug)
        if note.password is not None:
            raise PasswordRequiredException()
        content = note.get_content()
        return content

    @staticmethod
    def find_by_slug_and_password(slug: str, password: str) -> str:
        note = Note.__find_by_slug(slug)
        if note.password is None or not check_password(password, note.password):
            raise InvalidPasswordException()
        content = note.get_content()
        return decrypt(password, note.salt, content)

    def check_password_match(self):
        if self.fake_password != self.password:
            self.fake_password = None
            self.fake_content = None

    def generate_values(self):
        self.slug = generate_slug()
        if self.password is not None:
            self.salt = secrets.token_hex()[:Constants.SALT_LENGTH]

    def encrypt_note_data(self):
        if self.password is not None:
            self.content = encrypt(self.password, self.salt, self.content)
            self.password = make_password(self.password, self.salt, 'pbkdf2_sha256')

    def encrypt_fake_data(self):
        if self.fake_password is not None:
            self.fake_content = encrypt(self.fake_password, self.salt, self.fake_content)
            self.fake_password = make_password(self.fake_password, self.salt, 'pbkdf2_sha256')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self._state.adding is True:
            self.check_password_match()
            self.generate_values()
            self.encrypt_note_data()
            self.encrypt_fake_data()
        super(Note, self).save(force_insert, force_update, using, update_fields)

    def get_content(self) -> str:
        result = self.content if self.content else self.fake_content
        if self.content is not None:
            self.content = None
            self.save() if self.fake_content else self.delete()
        elif self.fake_content is not None:
            self.fake_content = None
            self.delete()
        return result
