from celery import Celery
from celery.schedules import crontab
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onetimelinks.settings')

app = Celery('onetimelinks')
app.config_from_object('django.conf:settings', namespace = 'CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'delete-notes': {
        'task': 'secnote.tasks.delete_notes',
        'schedule': crontab(),
    }
}