from celery import shared_task
from django.utils.timezone import now

from notes.models import Note


@shared_task
def delete_notes():
    timestamp = now()
    notes = Note.objects.filter(expires__lt=timestamp)
    notes.delete()
