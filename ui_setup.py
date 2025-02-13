import discord

ROTATE = '<:rotate:1339064241797202003>'
RIGHT = '<:move_right:1339064896859537428>'
LEFT = '<:move_left:1339064874520547338>'
UP = '<:move_up:1339065137386094632>'
DOWN = '<:move_down:1339064976790257674>'

class UIView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="", style=discord.ButtonStyle.success, emoji=ROTATE)
    async def button_rotate_callback(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("You clicked Button 1!", ephemeral=True)

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