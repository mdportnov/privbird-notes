from celery import shared_task
from django.core.mail import send_mail
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from notes.models import Note
from privbird import settings


def notify(note: Note, is_real: bool, is_destroyed: bool):
    subject: str = _('PrivBird notification')
    message: str = _('The {real} note with ID {id} has just been read, {ending}.').format(
        real='' if is_real else _('fake'),
        id=note.slug,
        ending=_('the content was destroyed') if is_destroyed
        else _('the next time someone reads it, a fake note will be displayed')
    )

    send_mail(
        subject, message.strip().capitalize(),
        settings.EMAIL_HOST_USER,
        [note.email], fail_silently=False,
    )


@shared_task
def delete_notes():
    timestamp = now()
    notes = Note.objects.filter(expires__lt=timestamp)
    notes.delete()
