import logging
import os
from aiogram import Bot, Dispatcher
from bot.handlers import BotHandlers
from discord_bot.client import DiscordClient


class TelegramBot:
    def __init__(self, discord_client):
        self.bot = Bot(token=os.getenv('TOKEN'))
        self.dp = Dispatcher()
        self.handlers = BotHandlers(self.bot)
        self.discord_client = discord_client

        self.handlers.set_discord_client(self.discord_client)

        # Реєструємо обробники
        self.handlers.register_handlers(self.dp)

        logging.info('Telegram бота ініціалізовано')

    async def start_polling(self):
        logging.info('Запуск Telegram бота')
        await self.dp.start_polling(self.bot)
