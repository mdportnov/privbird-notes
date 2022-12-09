from __future__ import annotations

import secrets
from typing import Optional

from cryptography.fernet import InvalidToken
from django.contrib.auth.hashers import check_password, make_password
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from notes.dto.exceptions.InvalidPassword import InvalidPasswordException
from notes.tasks import call_task, note_delete, note_update, notify
from notes.utils.Constants import Constants
from notes.utils.crypto import decrypt, encrypt
from notes.utils.generators import generate_key, generate_slug


class Note(models.Model):
    # Encryption key, if password is not set
    key: Optional[str] = None

    # Real content
    real_content = models.TextField(max_length=Constants.MAX_CONTENT_LENGTH, null=True)
    real_password = models.CharField(max_length=Constants.MAX_PASSWORD_LENGTH, default=None, null=True)
    real_notification = models.BooleanField(default=False)

    # Fake content
    fake_content = models.TextField(max_length=Constants.MAX_CONTENT_LENGTH, default=None, null=True)
    fake_password = models.TextField(max_length=Constants.MAX_PASSWORD_LENGTH, default=None, null=True)
    fake_notification = models.BooleanField(default=None, null=True)

    # Options
    expires = models.DateTimeField()
    email = models.EmailField(max_length=Constants.MAX_EMAIL_LENGTH, default=None, null=True)

    # Autogenerated
    salt = models.CharField(max_length=Constants.SALT_LENGTH, default=None, null=True)
    slug = models.SlugField(max_length=Constants.SLUG_LENGTH, unique=True, db_index=True)

    def validate(self) -> None:
        if self.real_content is None:
            raise serializers.ValidationError({'note': {'content': 'This field may not be null.'}})

        if self.real_password is None:
            if self.fake_password:
                raise serializers.ValidationError({'fake': {'password': 'This field must be null.'}})

        if self.real_notification is None:
            raise serializers.ValidationError({'note': {'content': 'This field may not be null.'}})

        if self.fake_content is None:
            if self.fake_password:
                raise serializers.ValidationError({'fake': {'password': 'This field must be null.'}})

            if self.fake_notification:
                raise serializers.ValidationError({'fake': {'notification': 'This field must be null.'}})

        if self.fake_content:
            if self.real_password:
                if self.fake_password is None:
                    raise serializers.ValidationError({'fake': {'password': 'This field may not be null.'}})

            if self.fake_notification is None:
                raise serializers.ValidationError({'fake': {'notification': 'This field may not be null.'}})

        if self.email is None:
            if self.real_notification or self.fake_notification:
                raise serializers.ValidationError({'options': {'email': 'This field may not be null.'}})

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        """
        Generate autogenerated values, encrypt content and save Note entity
        """
        if self._state.adding is True:
            self.__generate_values()
            self.__encrypt_note_data()
            self.__encrypt_fake_data()
        super(Note, self).save(force_insert, force_update, using, update_fields)

    def get_content(self, key: str) -> str:
        """
        Decrypt and return content
        """
        try:
            return self.__decrypt_content(key)
        except InvalidToken:
            raise InvalidPasswordException()

    def __str__(self) -> str:
        return f'Note {self.slug}'

    def __generate_values(self):
        """
        Generate auto generated Note values before save
        """
        self.slug = generate_slug()
        self.salt = secrets.token_hex()[:Constants.SALT_LENGTH]
        if self.real_password is None or (self.fake_content and self.fake_password is None):
            self.key = generate_key()

    def __encrypt_note_data(self):
        """
        Encrypt is_real Note content before save
        """
        key = self.real_password if self.real_password else self.key
        self.real_content = encrypt(key, self.salt, self.real_content)
        if self.real_password:
            self.real_password = make_password(self.real_password, self.salt, Constants.HASHER)

    def __encrypt_fake_data(self):
        """
        Encrypt fake Note content before save
        """
        if self.fake_content:
            key = self.fake_password if self.fake_password else self.key
            self.fake_content = encrypt(key, self.salt, self.fake_content)
        if self.fake_password:
            self.fake_password = make_password(self.fake_password, self.salt, Constants.HASHER)

    def __decrypt_content(self, key: str) -> str:
        """
        Return decrypted content and destroy it
        """
        if self.real_content and self.real_password and check_password(key, self.real_password):
            return self.__get_real_content(key)
        if self.fake_content and self.fake_password and check_password(key, self.fake_password):
            return self.__get_fake_content(key)
        return self.__get_real_content(key) if self.real_content else self.__get_fake_content(key)

    def __get_real_content(self, key: str) -> str:
        """
        Return decrypted is_real content and destroy it
        """
        content = decrypt(key, self.salt, self.real_content)
        is_destroyed = self.fake_content is None or self.real_password != self.fake_password
        self.__process_reading(is_destroyed, bool)
        return content

    def __get_fake_content(self, key: str) -> str:
        """
        Return fake content and destroy it
        """
        content = decrypt(key, self.salt, self.fake_content)
        is_destroyed = self.real_content is None or self.real_password != self.fake_password
        self.__process_reading(is_destroyed, bool)
        return content

    def __process_reading(self, is_destroyed: bool, is_real: bool):
        from notes.dto.NoteUpdateDto import NoteUpdateDto
        if is_real:
            self.real_content = None
        else:
            self.fake_content = None
        if not is_destroyed:
            call_task(note_update, dto=NoteUpdateDto.as_dto(self).serialize())
        else:
            call_task(note_delete, pk=self.pk)
        self.__notify_if_needed(is_real=is_real, is_destroyed=is_destroyed)

    def __notify_if_needed(self, is_real: bool, is_destroyed: bool):
        """
        Send email notification if needed
        """
        if is_real and self.real_notification or not is_real and self.fake_notification:
            message: str = _('The {is_real} note with ID {id} has just been read, {ending}.').format(
                real='' if is_real else _('fake'),
                id=self.slug,
                ending=_('the content was destroyed') if is_destroyed
                else _('the next time someone reads it, a fake note will be displayed')
            ).strip().capitalize()
            call_task(notify, email=self.email, message=message)
