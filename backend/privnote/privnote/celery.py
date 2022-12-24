import os

from celery import Celery
from celery.schedules import crontab
from kombu import Queue

from privnote import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'privnote.settings')

app = Celery('privnote')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.task_default_exchange = 'topic_notes'
app.conf.task_queues = tuple(Queue(queue, routing_key=queue) for queue in settings.CELERY_ALLOWED_QUEUES)
app.conf.task_default_queue = settings.CELERY_DEFAULT_QUEUE

app.conf.task_routes = {
    'notes.tasks.note_save': {'queue': settings.CELERY_DEFAULT_QUEUE}
}

app.conf.beat_schedule = {
    'delete-notes': {
        'task': 'notes.tasks.note_delete_expired',
        'schedule': crontab(),
    }
}
