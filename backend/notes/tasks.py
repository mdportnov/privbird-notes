from celery import shared_task
from django.template.defaulttags import now

from notes.models import Note


@shared_task
def delete_notes():
    timestamp = now()
    Note.objects.filter(expires__lt=timestamp).delete()
