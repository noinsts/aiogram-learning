from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers import BotHandlers
import asyncio
import os


load_dotenv()
TOKEN = os.getenv("TOKEN")


class WeatherBot:
    def __init__(self):
        self.bot = Bot(token=TOKEN)
        self.dp = Dispatcher()
        self.handlers = BotHandlers(self.bot)
        
        self.handlers.register_handlers(self.dp)

    async def run(self):
        try:
            print('Бот запущено!')
            await self.dp.start_polling(self.bot)
        finally:
            await self.bot.session.close()


if __name__ == "__main__":
    bot = WeatherBot()
    asyncio.run(bot.run())
