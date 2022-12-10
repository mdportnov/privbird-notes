import os

from celery import Celery
from celery.schedules import crontab

from privnote import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'privnote.settings')

app = Celery('privnote')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.task_default_routing_key = settings.CELERY_ROUTING_KEY

app.conf.beat_schedule = {
    'delete-notes': {
        'task': 'notes.tasks.note_delete_expired',
        'schedule': crontab(),
    }
}
