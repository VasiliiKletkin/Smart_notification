from .config import bot
from .models import Telegram


@bot.message_handler(commands=['start',])
def send_welcome(message):
  obj, created = Telegram.objects.update_or_create(
    user_id=message.from_user.id,
    defaults={"username": message.from_user.username,
               "first_name": message.from_user.first_name,
               "last_name": message.from_user.last_name
               }
    )
  bot.send_message(message.chat.id, "Hi, I will post new ads here, move to smartnotification.ru")
  bot.send_message(message.chat.id, f"your ID:{obj.user_id}, your username:{obj.username}")

