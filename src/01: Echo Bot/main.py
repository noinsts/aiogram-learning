import asyncio
import os

from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv
from aiogram import Dispatcher, types, Bot, Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

load_dotenv()
TOKEN = os.getenv("TOKEN")

class EchoBot:
    def __init__(self):
        self.bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
        self.dp = Dispatcher(storage=MemoryStorage())
        self.router = Router()

        self.router.message.register(self.start_handler, CommandStart())
        self.router.message.register(self.echo_handler)

        self.dp.include_router(self.router)

    async def start_handler(self, message: Message):
        await message.answer(f'Привіт, {message.from_user.first_name}! Я EchoBot. Напиши мені щось, а я відправлю тобі те саме')

    async def echo_handler(self, message: Message):
        await message.answer(f'Ти написав {message.text}')

    async def run(self):
        try:
            print('Бот запущено!')
            await self.dp.start_polling(self.bot)
        finally:
            await self.bot.session.close()


if __name__ == "__main__":
    bot = EchoBot()
    asyncio.run(bot.run())
