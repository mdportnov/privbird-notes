from django.db.models.signals import pre_delete
from django.dispatch import receiver

from .models import *


@receiver(pre_delete, sender = Note)
def delete_notes(sender, instance, **kwargs):
    Notification.objects.filter(id = instance.option.notification.id).delete()
    FakeNote.objects.filter(id = instance.option.fake_note.id).delete()
    Option.objects.filter(id = instance.option.id).delete()