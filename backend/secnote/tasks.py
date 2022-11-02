from celery import shared_task

from django.db.models import F, Q
from django.utils.timezone import now

from .models import Note


@shared_task
def delete_notes():
    Note.objects.filter(option__expiration_time__lt = now()).delete()
    Note.objects.filter(Q(option__confirmation__gt = 0) &
                        ~Q(option__password = F('option__fake_note__password'))).delete()
    Note.objects.filter(Q(option__confirmation__gt = 1) &
                        Q(option__password = F('option__fake_note__password'))).delete()
    Note.objects.filter(Q(option__confirmation = True) & Q(option__falsification = False)).delete()