import os

from dotenv import load_dotenv
from telebot import TeleBot

load_dotenv()

TOKEN = os.getenv("TOKEN")

bot = TeleBot(TOKEN, threaded=False)
