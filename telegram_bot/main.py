import asyncio
import logging
import os

import aiohttp
import aioschedule
from aiogram import Bot, Dispatcher, executor, types

TOKEN = os.getenv("TOKEN")
BASE_URL ="http://web:8000/"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Configure logging
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start',])
async def send_welcome(message: types.Message):
    await message.answer("I will tell you if something changes")


async def sending_messages():
    url_get_ads = BASE_URL + "api/v1/ads/?is_sent=false"
    async with aiohttp.ClientSession() as session:
        ads = []
        async with session.get(url_get_ads) as resp:
            if resp.status:
                ads = await resp.json()

        for ad in ads:
            message = f'New ad : {ad["ticket"]["title"]} {ad["url"]}'
            res = await bot.send_message(ad["ticket"]["telegram_id"], message)
            if res:
                url_sent = BASE_URL + f'api/v1/ads/{ad["id"]}/sent/'
                async with session.get(url_sent) as resp:
                    if not resp:
                        print("ERROR")


async def scheduler():
    aioschedule.every(int(1)).minutes.do(sending_messages)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

async def on_startup(_):
    asyncio.create_task(scheduler())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
