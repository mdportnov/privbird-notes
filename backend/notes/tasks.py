from celery import shared_task
from django.core.mail import send_mail
from django.utils.timezone import now

from notes.models import Note
from notes.utils.EmailNotification import EmailNotification
from privbird import settings


def notify(note: Note, is_real: bool, is_destroyed: bool):
    message = EmailNotification.build(is_real, is_destroyed, note.slug)

    subject = EmailNotification.subject.en
    content = message.en
    if note.language == Note.Language.RU:
        subject = EmailNotification.subject.ru
        content = message.ru

    send_mail(
        subject, content,
        settings.EMAIL_HOST_USER,
        [note.email], fail_silently=False,
    )


@shared_task
def delete_notes():
    timestamp = now()
    notes = Note.objects.filter(expires__lt=timestamp)
    notes.delete()
