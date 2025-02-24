import discord
import subprocess

TURN = '<:rotate:1339064241797202003>'
RIGHT = '<:move_right:1339064896859537428>'
LEFT = '<:move_left:1339064874520547338>'
UP = '<:move_up:1339065137386094632>'
DOWN = '<:move_down:1339064976790257674>'

def update_orientation():
    # Prev camera orientation then new one
    with open('camera_orientation.txt', "r") as file:
        content = file.read().strip()
    with open("camera_orientation.txt", 'w') as file:
        if content == '50, 135, 0, 230, 135, 0':
            file.write('230, 135, 0, 50, 135, 0')
        else:
            file.write('50, 135, 0, 230, 135, 0')

class UIView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label="", style=discord.ButtonStyle.success, emoji=TURN)
    async def button_turn_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        with open("message_id.txt", "r") as text_file:
            message_id = int(text_file.read().strip())

        channel = interaction.channel
        message = await channel.fetch_message(message_id)

        old_embed = message.embeds[0] # Have to make a temp embed to display the rendering title
        old_embed.title = 'Rendering'
        old_embed.color = 0xff0000 # Red
        old_file = message.attachments
        print(old_file)
        await message.edit(embed=old_embed, attachments=old_file)

        update_orientation()
        gif_path = rotate_cube()
        new_embed = get_embed(gif_path)
        file = discord.File(gif_path)

        # Edit the message with the new embed and file
        await message.edit(embed=new_embed, attachments=[file])

        with open("fast_setting.txt", "r") as text_file:
            is_fast = bool(text_file.read())
        if not is_fast:
            image_path = show_cube()
            new_embed = get_embed(image_path)
            file = discord.File(image_path)
            await message.edit(embed=new_embed, attachments=[file])

    @discord.ui.button(label="L", style=discord.ButtonStyle.primary)
    async def button_left_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        with open("message_id.txt", "r") as text_file:
            message_id = int(text_file.read().strip())

        channel = interaction.channel
        message = await channel.fetch_message(message_id)

        old_embed = message.embeds[0] # Have to make a temp embed to display the rendering title
        old_embed.title = 'Rendering'
        old_embed.color = 0xff0000 # Red
        old_file = message.attachments
        await message.edit(embed=old_embed, attachments=old_file)

        with open("message_id.txt", "r") as text_file:
            message_id = int(text_file.read().strip())
        
        with open("camera_orientation.txt", 'r') as file:
            content = file.read().strip()
            if content == '50, 135, 0, 230, 135, 0':
                move = 'B'
            else:
                move = 'L'

        with open("move.txt", "w") as text_file:
            text_file.write(move)
            
        gif_path = turn_cube()
        new_embed = get_embed(gif_path)
        file = discord.File(gif_path)

        # Edit the message with the new embed and file
        await message.edit(embed=new_embed, attachments=[file])

    @discord.ui.button(label="F", style=discord.ButtonStyle.primary)
    async def button_right_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        with open("message_id.txt", "r") as text_file:
            message_id = int(text_file.read().strip())

        channel = interaction.channel
        message = await channel.fetch_message(message_id)

        old_embed = message.embeds[0] # Have to make a temp embed to display the rendering title
        old_embed.title = 'Rendering'
        old_embed.color = 0xff0000 # Red
        old_file = message.attachments
        await message.edit(embed=old_embed, attachments=old_file)

        with open("message_id.txt", "r") as text_file:
            message_id = int(text_file.read().strip())
        
        with open("camera_orientation.txt", 'r') as file:
            content = file.read().strip()
            if content == '50, 135, 0, 230, 135, 0':
                move = 'R'
            else:
                move = 'F'

        with open("move.txt", "w") as text_file:
            text_file.write(move)

        gif_path = turn_cube()
        new_embed = get_embed(gif_path)
        file = discord.File(gif_path)

        # Edit the message with the new embed and file
        await message.edit(embed=new_embed, attachments=[file])
    
    @discord.ui.button(label="U", style=discord.ButtonStyle.primary)
    async def button_up_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        with open("message_id.txt", "r") as text_file:
            message_id = int(text_file.read().strip())

        channel = interaction.channel
        message = await channel.fetch_message(message_id)

        old_embed = message.embeds[0] # Have to make a temp embed to display the rendering title
        old_embed.title = 'Rendering'
        old_embed.color = 0xff0000 # Red
        old_file = message.attachments
        await message.edit(embed=old_embed, attachments=old_file)

        with open("message_id.txt", "r") as text_file:
            message_id = int(text_file.read().strip())
        
        with open("camera_orientation.txt", 'r') as file:
            content = file.read().strip()
            if content == '50, 135, 0, 230, 135, 0':
                move = 'D'
            else:
                move = 'U'

        with open("move.txt", "w") as text_file:
            text_file.write(move)

        gif_path = turn_cube()
        new_embed = get_embed(gif_path)
        file = discord.File(gif_path)

        # Edit the message with the new embed and file
        await message.edit(embed=new_embed, attachments=[file])

def get_embed(manim_output):
    embed = discord.Embed(
        title=f"Rubik's Cube",
        color=0x00ff00  # Green color
	)
    if manim_output:
        file_name = manim_output.split("/")[-1]  # Extract the file name from the path
        embed.set_image(url=f"attachment://{file_name}")

    return embed

def turn_cube():
    settings = [
        "py",
        "-m",
        "manim",
        "-ql",
        "--format=gif",
        "--disable_caching",
        "manim_code.py",
        "Turn"
    ]
    path = 'media/videos/manim_code/480p15/Turn_ManimCE_v0.19.0.gif'
    with open("fast_setting.txt", "r") as text_file:
        is_fast = text_file.read()
    
    if is_fast == 'True':
        settings[4] = '-s'
        path = 'media/images/manim_code/Turn_ManimCE_v0.19.0.png'

    subprocess.run(settings, shell=True)
    with open("state.txt","r") as f:
        state = f.read()
    if state == 'YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW':
        with open("cubesolved.txt", "w") as text_file:
            text_file.write('True')

    
    return path

def show_cube():
    settings = [
        "py",
        "-m",
        "manim",
        "-ql",
        "-s",
        "--disable_caching",
        "manim_code.py",
        "Show"
    ]
    subprocess.run(settings, shell=True)
    return 'media/images/manim_code/Show_ManimCE_v0.19.0.png'

def rotate_cube():
    settings = [
        "py",
        "-m",
        "manim",
        "-ql",
        "--format=gif",
        "--disable_caching",
        "manim_code.py",
        "Rotate"
    ]
    path = 'media/videos/manim_code/480p15/Rotate_ManimCE_v0.19.0.gif'
    with open("fast_setting.txt", "r") as text_file:
        is_fast = text_file.read()
    
    print(is_fast + '')
    if is_fast == 'True':
        settings[4] = '-s'
        path = 'media/images/manim_code/Rotate_ManimCE_v0.19.0.png'
    subprocess.run(settings, shell=True)
    return path