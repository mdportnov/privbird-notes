from celery import shared_task
from django.core.mail import send_mail
from django.utils.timezone import now

from notes.models import Note
from notes.utils.EmailNotification import EmailNotification
from privbird import settings


def notify(note: Note, is_real: bool):
    has_fake = note.fake_content is not None
    notification = EmailNotification(is_real=is_real, has_fake=has_fake, slug=note.slug)

    content = notification.content.en
    subject = notification.subject.en
    if note.language == Note.Language.RU:
        subject = notification.subject.ru
        content = notification.content.ru

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
