from django_search.celery import app

from .config import bot
from ads.models import Ad


@app.task
def send_ads():
    ads = Ad.objects.filter(is_sent=False).select_related("ticket", "ticket__telegram")
    
    for ad in ads:
        message = f"{ad.ticket.title}:{ad.title} {ad.url}"
        user_id = ad.ticket.telegram.user_id
        bot.send_message(user_id, message)
    ads.update(is_sent=True)