import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_search.settings')

app = Celery('django_search')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Celery Beat Settings

app.conf.beat_schedule = {

    "parse_data": {
        "task": "tickets.tasks.parse_data",
        "schedule": crontab(minute="*/1"),
    },
        "send_ads": {
        "task": "ads.tasks.send_ads",
        "schedule": crontab(minute="*/1"),
    },
}

