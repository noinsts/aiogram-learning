import asyncio
import os
from dotenv import load_dotenv
from aiogram.client.default import DefaultBotProperties
from aiogram import Bot, Dispatcher, types, Router
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command, CommandObject
from database import Database

load_dotenv()
TOKEN = os.getenv("TOKEN")


class TodoList:
    def __init__(self):
        self.bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
        self.dp = Dispatcher(storage=MemoryStorage())
        self.router = Router()
        self.db = Database()

        self.router.message.register(self.start_handler, CommandStart())
        self.router.message.register(self.add_todo_handler, Command('add'))
        self.router.message.register(self.todolist_handler, Command('list'))

        self.dp.include_router(self.router)

    async def start_handler(self, message: Message):
        await message.answer(f'Вітаю, {message.from_user.first_name}! '
                             f'Я бот Todolist. Додай задачу за допомогою /add.'
                             f'Подивись всі задачі за допомогою /list')

    async def add_todo_handler(self, message: Message, command: CommandObject):
        if command.args:
            user_id = message.from_user.id
            name = command.args
            self.db.add_todo(user_id, name)
            await message.answer(f'Успіх! Завдання {name} додано.')
        else:
            await message.answer('Ви не додали назву задачі')

    async def todolist_handler(self, message: Message):
        user_id = message.from_user.id
        result = self.db.get_todoes(user_id)
        await message.answer(result)

    async def run(self):
        try:
            print('Бот запущено!')
            await self.dp.start_polling(self.bot)
        finally:
            await self.bot.session.close()

if __name__ == "__main__":
    bot = TodoList()
    asyncio.run(bot.run())
