from aiogram.types import Message, CallbackQuery
from aiogram import Dispatcher
from aiogram.filters import CommandStart, Command
from bot.keyboards import get_main_keyboard
from discord_bot.client import DiscordClient


class BotHandlers:
    def __init__(self, bot):
        self.bot = bot
        self.ds = None

    def set_discord_client(self, discord_client):
        self.ds = discord_client

    async def start(self, message: Message):
        server_name = await self.ds.get_server_name()
        await message.answer(f'Вітаємо в пункті управлення сервером {server_name}.', reply_markup=get_main_keyboard())

    async def get_member_count_callback(self, callback_query: CallbackQuery):
        await callback_query.answer()
        count = await self.ds.get_member_count()
        await callback_query.message.answer(f'Кількість учасників на сервері: {count}')

    async def get_online_member_count_callback(self, callback_query: CallbackQuery):
        await callback_query.answer()
        count = await self.ds.get_online_member_count()
        await callback_query.message.answer(f'Кількість онлайн учасників на сервері: {count}')

    async def get_invoice_member_count_callback(self, callback_query: CallbackQuery):
        await callback_query.answer()
        count = await self.ds.get_invoice_member_count()
        await callback_query.message.answer(f'Кількість учасників в голосових каналах: {count}')

    def register_handlers(self, dp: Dispatcher):
        dp.message.register(self.start, CommandStart())
        dp.callback_query.register(self.get_member_count_callback, lambda c: c.data == "get_member_count")
        dp.callback_query.register(self.get_online_member_count_callback, lambda c: c.data == "get_online_member_count")
        dp.callback_query.register(self.get_invoice_member_count_callback, lambda c: c.data == "get_invoice_member_count")
