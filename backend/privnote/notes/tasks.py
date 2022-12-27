import asyncio
from datetime import datetime
from time import sleep
from typing import Dict
from uuid import uuid4

import redis
from celery import shared_task
from celery.beat import logger
from celery.result import allow_join_result
from django.core.mail import send_mail
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from notes.dto.NoteUpdateDto import NoteUpdateDto
from notes.dto.request.NoteCreateRequest import NoteCreateRequest
from notes.utils.Constants import Constants
from privnote import settings
from privnote.celery import app
from privnote.dto.exceptions.ExternalServerException import ExternalServerException
from privnote.dto.exceptions.UnknownQueueException import UnknownQueueException

conn = redis.StrictRedis(host=settings.REDIS_HOST, db=3)


def call_task(task, queue: str, **kwargs):
    if settings.DEBUG:
        return task(**kwargs)
    if queue not in settings.CELERY_ALLOWED_QUEUES:
        raise UnknownQueueException()
    with allow_join_result():
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
def note_append_result(task_id: str, slug: str):
    logger.info(f'Append for {task_id} result {slug}')
    conn.set(task_id, slug)


@app.task
def note_write(request: Dict, initial_queue: str, task_id: str):
    note = NoteCreateRequest.deserialize(request).as_note()
    note.save()
    slug = note.slug + (f'/{note.key}' if note.key else '')
    logger.info(f'Create note with slug {slug}')
    call_task(note_append_result, queue=initial_queue, task_id=task_id, slug=slug)


@app.task
def wait_for_response(task_id: str) -> str:
    logger.info(f'Wait for {task_id}')
    start = datetime.now()
    while not conn.exists(task_id):
        if (datetime.now() - start).seconds > Constants.MAX_WAITING_PERIOD:
            raise ExternalServerException()
        asyncio.sleep(0.1)
    return conn.getdel(task_id).decode('utf-8')


@app.task
def note_save(request: Dict, initial_queue: str, destination_queue: str) -> str:
    task_id = str(uuid4())
    logger.info(f'Save note from {initial_queue} to {destination_queue}')
    call_task(note_write, queue=destination_queue, request=request, initial_queue=initial_queue, task_id=task_id)
    return call_task(wait_for_response, queue=initial_queue, task_id=task_id)


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
