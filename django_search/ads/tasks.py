from bot.config import bot

from django_search.celery import app

from .models import Ad


@app.task
def send_ads():
    ads = Ad.objects.filter(is_sent=False)
    for ad in ads:
        message = f"New ad : {ad.ticket.title} {ad.url}"
        user_id = ad.ticket.telegram.user_id
        bot.send_message(user_id, message)
    ads.update(is_sent=True)


@app.task
def delete_old_ads():
    from datetime import datetime, timedelta

    end_datetime = datetime.now() - timedelta(days=7)
    Ad.objects.filter(create_at__lte=end_datetime).delete()
