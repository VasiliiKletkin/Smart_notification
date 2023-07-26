from django_search.celery import app

from .models import Ad


@app.task
def delete_old_ads():
    from datetime import datetime, timedelta

    end_datetime = datetime.now() - timedelta(days=7)
    Ad.objects.filter(created_at__lte=end_datetime).delete()
