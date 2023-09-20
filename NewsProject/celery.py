import os

from celery.schedules import crontab

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsProject.settings')

app = Celery('NewsProject')
app.config_from_object('django.conf:settings', namespace = 'CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_weekly_messages':{
        'task': 'application.tasks.week_notifications',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
        'args': (),
    },
}


