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

@bot.command()
async def cube(ctx):
    global df
    global cube_obj

    manim_output = ui_setup.show_cube()

    UI_view = ui_setup.UIView()
    UI_embed = ui_setup.get_embed(manim_output)

    file = discord.File(manim_output)

    message = await ctx.send(file=file, embed=UI_embed, view=UI_view)
    with open("message_id.txt", "w") as text_file:
        text_file.write(str(message.id))

@bot.command()
async def fast(ctx):
    print("Fast setting enabled")
    await ctx.send("Fast setting enabled, !slow to disable.")
    with open("fast_setting.txt", "w") as text_file:
        text_file.write('True')

@bot.command()
async def slow(ctx):
    print("Fast setting disabled")
    await ctx.send("Fast setting disabled, !fast to enable.")
    with open("fast_setting.txt", "w") as text_file:
        text_file.write('False')

bot.run(config.api_key, log_handler=config.handler) 