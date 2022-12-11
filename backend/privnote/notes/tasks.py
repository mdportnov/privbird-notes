from typing import Dict

from celery import shared_task
from celery.beat import logger
from django.core.mail import send_mail
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from notes.dto.NoteUpdateDto import NoteUpdateDto
from notes.dto.request.NoteCreateRequest import NoteCreateRequest
from privnote import settings
from privnote.celery import app


def call_task(task, **kwargs):
    if settings.DEBUG:
        return task(**kwargs)
    queue = kwargs.pop('queue') if 'queue' in kwargs else settings.CELERY_DEFAULT_QUEUE
    return task.apply_async(kwargs=kwargs, queue=queue).get()


@app.task
def notify(email: str, message: str):
    logger.info(f'Send email notification for {email}')
    send_mail(
        subject=_('PrivBird notification'),
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False,
    )


@app.task
def note_save(request: Dict) -> str:
    note = NoteCreateRequest.deserialize(request).as_note()
    note.save()
    return note.slug + (f'/{note.key}' if note.key else '')


@app.task
def note_update(dto: Dict):
    from notes.models import Note
    dto = NoteUpdateDto.deserialize(dto)
    note = Note.objects.filter(id=dto.id).first()
    dto.apply(note).save()


@app.task
def note_delete(pk: int):
    from notes.models import Note
    Note.objects.filter(pk=pk).delete()


@shared_task
def note_delete_expired():
    from notes.models import Note
    timestamp = now()
    notes = Note.objects.filter(expires__lt=timestamp)
    notes.delete()
