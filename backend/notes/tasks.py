from celery import shared_task
from celery.beat import logger
from django.core.mail import send_mail
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from notes.models import Note
from privbird import settings
from privbird.celery import app


@app.task
def notify(email: str, message: str):
    logger.info(f'Notification for {email}: {message}')
    print('kek')
    send_mail(
        subject=_('PrivBird notification'),
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False,
    )


@shared_task
def delete_notes():
    timestamp = now()
    notes = Note.objects.filter(expires__lt=timestamp)
    notes.delete()
