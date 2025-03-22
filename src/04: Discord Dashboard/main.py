import asyncio
import logging

from dotenv import load_dotenv

from bot.bot import TelegramBot
from discord_bot.client import DiscordClient


logging.basicConfig(level=logging.INFO)

async def main():
    load_dotenv()

    discord_client = DiscordClient()

    discord_task = asyncio.create_task(discord_client.start())

    await asyncio.sleep(2)

    telegram_bot = TelegramBot(discord_client)
    await telegram_bot.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
