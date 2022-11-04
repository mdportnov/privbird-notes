from celery import shared_task
from django.utils.timezone import now

from notes.models import Note
from notes.utils.EmailNotifications import EmailNotifications
from privbird.messages.Message import Message


def notify(note: Note, is_real: bool):
    subject = EmailNotifications.subject
    notification = EmailNotifications.notification
    fake = EmailNotifications.fake if not is_real else Message()
    has_fake = EmailNotifications.has_fake if is_real and note.fake_notification else None

    print(notification)
    # send_mail(
    #     EmailNotifications.subject,
    #     notification.format(slug),
    #     settings.EMAIL_HOST_USER,
    #     [email], fail_silently=False,
    # )


@shared_task
def delete_notes():
    timestamp = now()
    notes = Note.objects.filter(expires__lt=timestamp)
    notes.delete()
