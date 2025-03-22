import os
import logging
import discord
from discord.ext import commands

class DiscordClient:
    def __init__(self):
        self.token = os.getenv("DISCORD_TOKEN")
        self.server_id = int(os.getenv("DISCORD_SERVER_ID"))

        intents = discord.Intents.default()
        intents.members = True
        intents.presences = True

        self.client = commands.Bot(command_prefix='.', intents=intents)

        @self.client.event
        async def on_ready():
            self._ready = True
            self.server = self.client.get_guild(self.server_id)

            if self.server:
                logging.info(f'Бот підключено як {self.client.user}')
                logging.info(f'Сервер {self.server.name} знайдено')
            else:
                logging.info(f'Не вдалося встановити підключення з сервером {self.server_id}')
                self._ready = False

        self._ready = False
        logging.info('Діскорд кліент ініціалізовано')

    async def start(self):
        logging.info('Запуск Discord клієнта')
        await self.client.start(self.token)

    def is_ready(self):
        return self._ready

    async def get_member_count(self):
        if self.server:
            return self.server.member_count
        return 'Невідомий сервер'

    async def get_online_member_count(self):
        online_members = 0

        if self.server:
            for member in self.server.members:
                if member.status != discord.Status.offline:
                    online_members += 1

        return online_members

    async def get_invoice_member_count(self):
        voice_member = 0

        if self.server:
            for voice_channel in self.server.voice_channels:
                voice_member += len(voice_channel.members)

        return voice_member

    async def get_server_name(self):
        if self.server:
            try:
                return self.server.name
            except AttributeError:
                return "Не вдалося отримати ім'я серверу"
        else:
            return 'Сервер не знайдено'
