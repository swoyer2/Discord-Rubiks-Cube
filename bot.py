import discord
from discord.ext import commands

import config
import ui_setup

discord.VoiceClient.warn_nacl = False
intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

bot.run(config.api_key, log_handler=config.handler) 