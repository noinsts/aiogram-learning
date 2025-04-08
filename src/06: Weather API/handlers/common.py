from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from .base import BaseHandler

from keyboards.reply import MainMenuKeyboard


class CommonHandlers(BaseHandler):
    def register_handlers(self):
        self.router.message.register(self.cmd_start, CommandStart())
        self.router.message.register(self.cmd_help, Command('help'))

    async def cmd_start(self, message: Message):
        await message.answer(
            "Вітаємо в боті з погодою!"
            "Ви можете дізнатись прогноз погоди в вашому місті за допомогою /weather",
            reply_markup=MainMenuKeyboard().get_keyboard()
        )

    async def cmd_help(self, message: Message):
        pass
