import asyncio
import logging
import os

import aiohttp
import aioschedule
from aiogram import Bot, Dispatcher, executor, types

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Configure logging
logging.basicConfig(level=logging.INFO)



@dp.message_handler(commands=['start',])
async def send_welcome(message: types.Message):
    await message.answer("I will tell you if something changes")


async def sending_messages():
    url = "http://web:8000/api/v1/ads/?is_sent=false"
    async with aiohttp.ClientSession() as session:
        ads = []
        async with session.get(url) as resp:
            if resp.status:
                ads = await resp.json()

        for ad in ads:
            message = f'New ad : {ad["ticket"]["title"]} {ad["url"]}'
            res = await bot.send_message(ad["ticket"]["telegram_id"], message)
            if res:
                url_sent = f'http://web:8000/api/v1/ads/{ad["id"]}/sent/'
                async with session.get(url_sent) as resp:
                    if not resp:
                        print("ERROR")


async def scheduler():
    aioschedule.every(int(2)).minutes.do(sending_messages)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

async def on_startup(_):
    asyncio.create_task(scheduler())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
