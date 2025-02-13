import discord
import subprocess

TURN = '<:rotate:1339064241797202003>'
RIGHT = '<:move_right:1339064896859537428>'
LEFT = '<:move_left:1339064874520547338>'
UP = '<:move_up:1339065137386094632>'
DOWN = '<:move_down:1339064976790257674>'

def update_orientation(phi_change, theta_change, gamma_change):
    with open('camera_orientation.txt', "r") as file:
            content = file.read().strip()
    values = content.split(",")
    with open("camera_orientation.txt", 'w') as file:
        file.write(f'{int(values[0])+phi_change}, {int(values[1]) + theta_change}, {int(values[2]) + gamma_change}')

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
        update_orientation(0, -90, 0)

        with open("message_id.txt", "r") as text_file:
            message_id = int(text_file.read().strip())
            
        channel = interaction.channel
        message = await channel.fetch_message(message_id)

        gif_path = rotate_cube()
        new_embed = get_embed(gif_path)
        file = discord.File(gif_path)

        # Edit the message with the new embed and file
        await message.edit(embed=new_embed, attachments=[file])

    @discord.ui.button(label="", style=discord.ButtonStyle.primary, emoji=RIGHT)
    async def button_right_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        update_orientation(0, 90, 0)

        with open("message_id.txt", "r") as text_file:
            message_id = int(text_file.read().strip())
            
        channel = interaction.channel
        message = await channel.fetch_message(message_id)

        gif_path = rotate_cube()
        new_embed = get_embed(gif_path)
        file = discord.File(gif_path)

        # Edit the message with the new embed and file
        await message.edit(embed=new_embed, attachments=[file])
    
    @discord.ui.button(label="", style=discord.ButtonStyle.primary, emoji=UP)
    async def button_up_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        update_orientation(-90, 0, -30)

        with open("message_id.txt", "r") as text_file:
            message_id = int(text_file.read().strip())
            
        channel = interaction.channel
        message = await channel.fetch_message(message_id)

        gif_path = rotate_cube()
        new_embed = get_embed(gif_path)
        file = discord.File(gif_path)

        # Edit the message with the new embed and file
        await message.edit(embed=new_embed, attachments=[file])

    @discord.ui.button(label="", style=discord.ButtonStyle.primary, emoji=DOWN)
    async def button_down_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        update_orientation(90, 0, 30)

        with open("message_id.txt", "r") as text_file:
            message_id = int(text_file.read().strip())
            
        channel = interaction.channel
        message = await channel.fetch_message(message_id)

        gif_path = rotate_cube()
        new_embed = get_embed(gif_path)
        file = discord.File(gif_path)

        # Edit the message with the new embed and file
        await message.edit(embed=new_embed, attachments=[file])

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

def rotate_cube():
    subprocess.run([
        "py",
        "-m",
        "manim",
        "-ql",
        "--format=gif",
        "manim_code.py",
        "Rotate"
    ], shell=True)
    return 'media/videos/manim_code/480p15/Rotate_ManimCE_v0.19.0.gif'