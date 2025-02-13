import discord
import subprocess

TURN = '<:rotate:1339064241797202003>'
RIGHT = '<:move_right:1339064896859537428>'
LEFT = '<:move_left:1339064874520547338>'
UP = '<:move_up:1339065137386094632>'
DOWN = '<:move_down:1339064976790257674>'

class UIView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="", style=discord.ButtonStyle.success, emoji=TURN)
    async def button_turn_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        with open("message_id.txt", "r") as text_file:
            message_id = int(text_file.read().strip())
            
        channel = interaction.channel
        message = await channel.fetch_message(message_id)

        gif_path = turn_cube()
        new_embed = get_embed(gif_path)
        file = discord.File(gif_path)

        # Edit the message with the new embed and file
        await message.edit(embed=new_embed, attachments=[file])

    @discord.ui.button(label="", style=discord.ButtonStyle.primary, emoji=LEFT)
    async def button_left_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("You clicked Button 2!", ephemeral=True)

    @discord.ui.button(label="", style=discord.ButtonStyle.primary, emoji=RIGHT)
    async def button_right_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("You clicked Button 2!", ephemeral=True)
    
    @discord.ui.button(label="", style=discord.ButtonStyle.primary, emoji=UP)
    async def button_up_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("You clicked Button 2!", ephemeral=True)

    @discord.ui.button(label="", style=discord.ButtonStyle.primary, emoji=DOWN)
    async def button_down_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("You clicked Button 2!", ephemeral=True)

def get_embed(manim_output):
    embed = discord.Embed(
        title=f"Rubik's Cube",
        color=0xff0000  # Red color
	)
    if manim_output:
        file_name = manim_output.split("/")[-1]  # Extract the file name from the path
        embed.set_image(url=f"attachment://{file_name}")

    return embed

def turn_cube():
    subprocess.run([
        "py",
        "-m",
        "manim",
        "-ql",
        "--format=gif",
        "manim_code.py",
        "Turn"
    ], shell=True)
    return 'media/videos/manim_code/480p15/Turn_ManimCE_v0.19.0.gif'

def show_cube():
    subprocess.run([
        "py",
        "-m",
        "manim",
        "-ql",
        "--format=gif",
        "manim_code.py",
        "Show"
    ], shell=True)
    return 'media/videos/manim_code/480p15/Show_ManimCE_v0.19.0.gif'