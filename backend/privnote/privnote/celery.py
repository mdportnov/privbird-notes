import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'privnote.settings')

app = Celery('privnote')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'delete-notes': {
        'task': 'notes.tasks.delete_notes',
        'schedule': crontab(),
    }
}
