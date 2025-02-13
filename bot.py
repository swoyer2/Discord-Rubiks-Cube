import discord
from discord.ext import commands
from manim import *
import subprocess

import config
import ui_setup

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def cube(ctx):
    global df
    global cube_obj
    manim_output = 'media/videos/manim_code/480p15/Cube_ManimCE_v0.19.0.gif'

    UI_view = ui_setup.UIView()
    UI_embed = ui_setup.get_embed(manim_output)

    file = discord.File(manim_output)

    subprocess.run([
        "py",
        "-m",
        "manim",
        "-ql",
        "--format=gif",
        "manim_code.py",
        "Cube"
    ], shell=True)

    await ctx.send(file=file, embed=UI_embed, view=UI_view)

bot.run(config.api_key, log_handler=config.handler) 