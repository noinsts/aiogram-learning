"""
БОТ НЕ ПРАЦЮЄ, ОСКІЛЬКИ БІБЛІОТЕКА YEELIGHT
відмовляється працювати з моєю лампою (Xiaomi Mi Desk Lamp 1S)
"""


import asyncio
import os

from aiogram import Bot, Dispatcher
from handlers import BotHandler
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")


class LampBot:
    def __init__(self):
        self.bot = Bot(token=TOKEN)
        self.dp = Dispatcher()
        self.handlers = BotHandler(self.bot)

        self.handlers.register_handlers(self.dp)

    async def run(self):
        try:
            print('Бот запущено!')
            await self.dp.start_polling(self.bot)
        finally:
            await self.bot.session.close()

if __name__ == "__main__":
    bot = LampBot()
    asyncio.run(bot.run())
