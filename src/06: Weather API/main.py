from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import asyncio
import os
import sys
from logger import setup_logger

from aiogram.fsm.storage.memory import MemoryStorage

from handlers.common import CommonHandlers

# ця незрозуміла штука потрібна, щоб .env файл шукався в корні проекту
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), '.env')
load_dotenv(dotenv_path)
TOKEN = os.getenv("TOKEN")

# Додаємо поточну директорію до шляху пошуку
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


class WeatherBot:
    def __init__(self):
        self.bot = Bot(token=TOKEN)
        self.storage = MemoryStorage()
        self.dp = Dispatcher(storage=self.storage)
        self.log = setup_logger()

        self.register_routers()

    def register_routers(self):
        common_handler = CommonHandlers()

        self.dp.include_router(common_handler.router)


    async def run(self):
        try:
            self.log.info('Бот запущено!')
            await self.dp.start_polling(self.bot)
        finally:
            await self.bot.session.close()


if __name__ == "__main__":
    bot = WeatherBot()
    asyncio.run(bot.run())
