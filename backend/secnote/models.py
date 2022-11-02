from base64 import urlsafe_b64encode
from os import urandom

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from django.conf import settings
from django.contrib.auth.hashers import check_password, make_password
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.db import models
from django.shortcuts import reverse
from django.utils.timezone import now, timedelta
from nanoid import generate


def get_expiration_time(days):
    return now() + timedelta(days=days)


def generate_slug():
    return generate(size=12)


def generate_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=SHA256(),
        length=32,
        salt=bytes.fromhex(salt),
        iterations=390000,
    )
    return urlsafe_b64encode(kdf.derive(password.encode()))


def encrypt_content(password, salt, content):
    f = Fernet(generate_key(password, salt))
    return f.encrypt(content.encode()).decode()


def decrypt_content(password, salt, content):
    f = Fernet(generate_key(password, salt))
    return f.decrypt(content.encode()).decode()


class NotificationManager(models.Manager):
    def get_by_natural_key(self, main, fake, email):
        return self.get(main=main, fake=fake, email=email)


class Notification(models.Model):
    main = models.BooleanField(default=False)
    fake = models.BooleanField(default=False)
    email = models.EmailField(max_length=254, blank=True, null=True)


class FakeNoteManager(models.Manager):
    def get_by_natural_key(self, content, password, salt):
        return self.get(content=content, password=password, salt=salt)


class FakeNote(models.Model):
    content = models.TextField(blank=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    salt = models.CharField(max_length=32, blank=True)

    def prepare_content(self):
        self.password = make_password(str(self.password or ''), 'pbkdf2_sha256')
        self.salt = urandom(16).hex()
        self.content = encrypt_content(self.password, self.salt, self.content)


class OptionManager(models.Manager):
    def get_by_natural_key(self, type, auto_destruction, expiration_time, password,
                           salt, confirmation, notification, fake_note, falsification):
        return self.get(
            type=type,
            auto_destruction=auto_destruction,
            expiration_time=expiration_time,
            password=password,
            salt=salt,
            confirmation=confirmation,
            notification=notification,
            fake_note=fake_note,
            falsification=falsification,
        )

    def get_or_create_notification(self, validated_data):
        notification_data = validated_data.pop('notification')
        return Notification.objects.create(**notification_data)

    def get_or_create_fake_note(self, validated_data):
        fake_note_data = validated_data.pop('fake_note')
        return FakeNote.objects.create(**fake_note_data or {})

    def get_or_create(self, **validated_data):
        validated_data['notification'] = self.get_or_create_notification(validated_data)
        validated_data['fake_note'] = self.get_or_create_fake_note(validated_data)
        return super().create(**validated_data)


class Option(models.Model):
    type_choices = [
        ('HTTPS', 'HTTPS'),
        ('ONION', 'ONION'),
        ('I2P', 'I2P'),
    ]

    auto_destruction_choices = [
        ('AFTER_DAY', 'AFTER_DAY'),
        ('AFTER_WEEK', 'AFTER_WEEK'),
        ('AFTER_MONTH', 'AFTER_MONTH'),
        ('DEFAULT', 'DEFAULT'),
    ]

    expiration_time_choices = {
        'AFTER_DAY': 1,
        'AFTER_WEEK': 7,
        'AFTER_MONTH': 30,
        'DEFAULT': 365,
    }

    type = models.CharField(max_length=5, choices=type_choices, default='HTTPS')
    auto_destruction = models.CharField(max_length=11, choices=auto_destruction_choices, default='DEFAULT')
    expiration_time = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    salt = models.CharField(max_length=32, blank=True)
    confirmation = models.IntegerField(default=0)
    notification = models.ForeignKey(Notification, on_delete=models.SET_NULL, null=True)
    fake_note = models.ForeignKey(FakeNote, on_delete=models.SET_NULL, null=True)
    falsification = models.BooleanField(default=True)

    objects = OptionManager()

    def prepare_content(self):
        self.expiration_time = get_expiration_time(self.expiration_time_choices[self.auto_destruction])
        self.password = make_password(str(self.password or ''), 'pbkdf2_sha256')
        self.salt = urandom(16).hex()
        if not self.fake_note.content:
            self.falsification = False

        self.fake_note.prepare_content()
        self.save()

    def save(self, *args, **kwargs):
        self.fake_note.save()
        super().save(*args, **kwargs)


class NoteManager(models.Manager):
    def get_or_create(self, **validated_data):
        option_data = validated_data.pop('option')
        option = Option.objects.get_or_create(**option_data)
        validated_data['option'] = option
        return super().create(**validated_data)


class Note(models.Model):
    message_choices = {
        'READ': 'The {} note with ID ******{} was read the first time!',
        'READ_DESTROY': 'The {} note with ID ******{} was read and destroyed!',
    }

    slug = models.SlugField(default=generate_slug, unique=True)
    content = models.TextField()
    option = models.ForeignKey(Option, on_delete=models.SET_NULL, null=True)

    objects = NoteManager()

    def get_absolute_url(self):
        return reverse('note', kwargs={'slug': self.slug})

    def prepare_content(self):
        self.option.prepare_content()
        self.content = encrypt_content(self.option.password, self.option.salt, self.content)
        self.save()
        return self

    def manage_content(self):
        if self.option.password != self.option.fake_note.password:
            content = decrypt_content(self.option.password, self.option.salt, self.content)
            if self.option.notification.main:
                self.send_email(self.message_choices['READ_DESTROY'].format('main', self.slug[-6:]))
        else:
            if not self.option.confirmation:
                content = decrypt_content(self.option.password, self.option.salt, self.content)
                if self.option.notification.main:
                    self.send_email(self.message_choices['READ'].format('main', self.slug[-6:]))
            else:
                content = decrypt_content(self.option.fake_note.password,
                                          self.option.fake_note.salt, self.option.fake_note.content)
                if self.option.notification.fake:
                    self.send_email(self.message_choices['READ_DESTROY'].format('fake', self.slug[-6:]))

        self.option.confirmation += 1
        self.save()
        return content

    def get_content(self, password):
        if check_password(password, self.option.password):
            content = self.manage_content()
        elif check_password(password, self.option.fake_note.password):
            content = decrypt_content(self.option.fake_note.password,
                                      self.option.fake_note.salt, self.option.fake_note.content)
            if self.option.notification.fake:
                self.send_email(self.message_choices['READ_DESTROY'].format('fake', self.slug[-6:]))

            self.option.confirmation = 1
            self.save()
        else:
            raise PermissionDenied('Password is invalid')

        return content

    def send_email(self, message):
        send_mail(
            'Read notification',
            message,
            settings.EMAIL_HOST_USER,
            [self.option.notification.email],
            fail_silently=True,
        )

    def save(self, *args, **kwargs):
        self.option.save()
        super().save(*args, **kwargs)


class Support(models.Model):
    problem = models.TextField()
    email = models.EmailField(max_length=254, blank=True, null=True)
