import os

from django.core.management.base import BaseCommand
from dotenv import load_dotenv
from profiles.models import Telegram
from telebot import TeleBot

load_dotenv()

TOKEN = os.getenv("TOKEN")

bot = TeleBot(TOKEN, threaded=False)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  bot.send_message(message.chat.id, "Hi, I will post new ads here, move to smartnotification.ru")
  username = message.from_user.username
  id = message.from_user.id
  try:  
    Telegram.objects.create(username = username, telegram_id = id)
  except:
      pass


class Command(BaseCommand):
  	# Используется как описание команды обычно
    help = 'Implemented to Django application telegram bot setup command'

    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2) # Сохранение обработчиков
        bot.load_next_step_handlers()								# Загрузка обработчиков
        bot.infinity_polling()											# Бесконечный цикл бота


