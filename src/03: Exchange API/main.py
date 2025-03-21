import asyncio
import os
from aiogram import Bot, Dispatcher
from handlers import BotHandlers
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")


class CurrencyBot:
    def __init__(self):
        self.bot = Bot(token=TOKEN)
        self.dp = Dispatcher()
        self.handlers = BotHandlers(self.bot)

        self.handlers.register_handlers(self.dp)

    async def run(self):
        await self.dp.start_polling(self.bot)
        print('Бот запущено!')


if __name__ == "__main__":
    bot = CurrencyBot()
    asyncio.run(bot.run())
