from django_search.celery import app

from .management.commands.bot import bot
from .models import Ad


@app.task
def send_message(telegram_id, message):
    bot.send_message(telegram_id, message)


@app.task
def send_ads():
    ads = Ad.objects.filter(is_sent=False).select_related("ticket", "ticket__telegram")
    for ad in ads:
        message = f'New ad : {ad.ticket.title} {ad.url}'
        telegram_id = ad.ticket.telegram.telegram_id
        send_message.delay(telegram_id, message)
    ads.update(is_sent=True)
