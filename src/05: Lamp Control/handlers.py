import os
from dotenv import load_dotenv
from yeelight import Bulb

from aiogram.types import Message, CallbackQuery
from aiogram import Dispatcher
from aiogram.filters import CommandStart, Command

from keyboards import get_main_keyboard


class BotHandler:
    def __init__(self, bot):
        self.bot = bot
        self.bulb = Bulb(os.getenv("BULB_IP"))

    async def start(self, message: Message):
        await message.answer('Вітаємо в пункті керування лампою', reply_markup=get_main_keyboard())

    async def turn_on_lamp_callback(self, callback_query: CallbackQuery):
        self.bulb.turn_on()

    async def turn_off_lamp_callback(self, callback_query: CallbackQuery):
        pass

    async def brightness_20_callback(self, callback_query: CallbackQuery):
        pass

    async def brightness_50_callback(self, callback_query: CallbackQuery):
        pass

    async def brightness_100_callback(self, callback_query: CallbackQuery):
        pass

    def register_handlers(self, dp: Dispatcher):
        dp.message.register(self.start, CommandStart())
        dp.callback_query.register(self.turn_on_lamp_callback, lambda c: c.data == "turn_on_lamp")
        dp.callback_query.register(self.turn_off_lamp_callback, lambda c: c.data == 'turn_off_lamp')
        dp.callback_query.register(self.brightness_20_callback, lambda c: c.data == 'brightness_20')
        dp.callback_query.register(self.brightness_50_callback, lambda c: c.data == 'brightness_50')
        dp.callback_query.register(self.brightness_100_callback, lambda c: c.data == 'brightness_100')
