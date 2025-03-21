from aiogram.types import Message
from aiogram import Dispatcher
from aiogram.filters import CommandStart, Command, CommandObject

from exchange import ExchangeAPI


class BotHandlers:
    def __init__(self, bot):
        self.bot = bot
        self.api = ExchangeAPI()

    async def start(self, message: Message):
        await message.answer("Бот Exchange API. Напишіть /currency (валюту), щоб отримати курс")

    async def get_currency(self, message: Message, command: CommandObject):
        if command.args:
            currency = command.args
            rate = await self.api.get_exchange_rate(currency)
            await message.answer(f'Курс {currency}: {rate}')
        else:
            await message.answer('Ви не введи валюту')

    def register_handlers(self, dp: Dispatcher):
        dp.message.register(self.start, CommandStart())
        dp.message.register(self.get_currency, Command("currency"))