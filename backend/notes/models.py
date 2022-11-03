from __future__ import annotations

import secrets

from django.contrib.auth.hashers import check_password, make_password
from django.db import models

from notes.exceptions.InvalidPassword import InvalidPasswordException
from notes.exceptions.NoteNotFound import NoteNotFoundException
from notes.exceptions.PasswordRequired import PasswordRequiredException
from notes.utils.crypto import decrypt, encrypt
from notes.utils.expiration import Expiration
from notes.utils.slug import generate_slug


class Note(models.Model):
    class Network(models.TextChoices):
        HTTPS = 'HTTPS'
        TOR = 'TOR'
        I2P = 'I2P'

    content = models.TextField(null=True)

    password = models.CharField(max_length=100, default=None, blank=True, null=True)
    notification = models.BooleanField(default=False)

    fakeContent = models.TextField(default=None, blank=True, null=True)
    fakePassword = models.TextField(default=None, blank=True, null=True)
    fakeNotification = models.BooleanField(default=None, null=True)

    salt = models.CharField(max_length=32, default=None, blank=True, null=True)
    slug = models.SlugField(max_length=12, unique=True)
    network = models.CharField(max_length=5, choices=Network.choices, default=Network.HTTPS)
    expires = models.DateTimeField(default=Expiration.YEAR.get_expiration())
    email = models.EmailField(default=None, blank=True, null=True)

    def generate_values(self):
        self.slug = generate_slug()
        self.salt = secrets.token_hex(16)

    def encrypt_data(self):
        if self.password is not None:
            self.content = encrypt(self.password, self.salt, self.content)
            self.password = make_password(self.password, self.salt, 'pbkdf2_sha256')

    def encrypt_fake_data(self):
        if self.fakePassword is not None:
            self.fakeContent = encrypt(self.fakePassword, self.salt, self.fakeContent)
            self.fakePassword = make_password(self.fakePassword, self.salt, 'pbkdf2_sha256')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self._state.adding is True:
            self.generate_values()
            self.encrypt_data()
            self.encrypt_fake_data()
        super(Note, self).save(force_insert, force_update, using, update_fields)

    def process_read(self):
        if self.content is not None:
            self.content = None
            self.save() if self.fakeContent is not None else self.delete()
            # TODO send email content has been read
        elif self.fakeContent is not None:
            self.fakeContent = None
            self.delete()
            # TODO send email fake content has been read

    @staticmethod
    def find_by_slug(slug: str) -> str:
        if not Note.objects.filter(slug=slug).exists():
            raise NoteNotFoundException()
        note = Note.objects.get(slug=slug)
        if note.password is not None:
            raise PasswordRequiredException()
        content = note.content if note.content is not None else note.fakeContent
        note.process_read()
        return content

    @staticmethod
    def find_by_slug_and_password(slug: str, password: str) -> str:
        if not Note.objects.filter(slug=slug).exists():
            raise NoteNotFoundException()
        note = Note.objects.get(slug=slug)
        if note.password is not None and not check_password(password, note.password):
            raise InvalidPasswordException()
        content = note.content if note.content is not None else note.fakeContent
        note.process_read()
        return decrypt(password, note.salt, content)
