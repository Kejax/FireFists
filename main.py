import discord
from discord.ext import commands
import aiomysql
import aiohttp
import os
import jenv
import logging
import datetime

command_prefix = commands.when_mentioned_or("!")
intents = discord.Intents.all()
case_insensitive = True
description = "The FireFists Bot"
strip_after_prefix = True
owner_ids = [538029972791492609, 713413872194682881, 833694505663201349]

bot = commands.Bot(
    command_prefix=command_prefix,
    intents=intents,
    case_insensitiv=case_insensitive,
    description=description,
    owner_ids=owner_ids,
    strip_after_prefix=strip_after_prefix
)

bot.logger = logging.getLogger('discord')
bot.logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('[%(asctime)s][%(levelname)s]: %(message)s'))
bot.logger.addHandler(handler)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter('[%(asctime)s][%(levelname)s]: %(message)s'))
bot.logger.addHandler(stream_handler)

bot.is_ready = False

extensions = [
    "cogs.verify"
]


@bot.event
async def on_ready():
    if not bot.is_ready:
        bot.logger.info(f"Logged in as {bot.user}")
        bot.is_ready = True
        for extension in extensions:
            await bot.load_extension(extension)


bot.run(jenv.getenv("TOKEN"))
