import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_search.settings")

app = Celery("django_search")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

# Celery Beat Settings

app.conf.beat_schedule = {
    "send_ads": {
        "task": "bot.tasks.send_ads",
        "schedule": crontab(minute="*/5"),
    },
    "delete_old_ads": {
        "task": "ads.tasks.delete_old_ads",
        "schedule": crontab(hour="*/12"),
    },
    "run_spiders":{
        "task": "scraper.tasks.run_spiders",
        "schedule": crontab(minute="*/5"),
    },
}
