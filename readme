# Discord Rubik's Cube Bot

This is a Discord bot that allows users to interact with a virtual Rubik's Cube. The bot provides commands to manipulate the cube and visualize the changes in real-time using the Manim library.

## Features

- Display a Rubik's Cube and its current state.
- Rotate the cube using interactive buttons.
- Toggle between fast and slow rendering modes.

## Prerequisites

- Python 3.8 or higher
- [Discord.py](https://discordpy.readthedocs.io/en/stable/) library
- [Manim](https://docs.manim.community/en/stable/) library
- [Manim Rubik's Cube](https://github.com/ManimCommunity/manim-rubikscube) plugin
- [MagicCube](https://pypi.org/project/magiccube/) library

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/swoyer2/Discord-Rubiks-Cube.git
   cd Discord-Rubiks-Cube
   ```

2. **Install the required Python packages:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the bot:**

   - Create a `config.py` file in the root directory with your Discord bot token and any other necessary configurations. The file should look like this:

     ```python
     api_key = 'YOUR_DISCORD_BOT_TOKEN'
     handler = None  # or configure a logging handler if needed
     ```

   - Ensure that `config.py` is listed in your `.gitignore` to keep your token secure.

4. **Run the bot:**

   Execute the following command to start the bot:

   ```bash
   python bot.py
   ```

## Usage

- **Commands:**
  - `!cube`: Displays the current state of the Rubik's Cube.
  - `!fast`: Enables fast rendering mode.
  - `!slow`: Disables fast rendering mode.

- **Interactive Buttons:**
  - Use the buttons labeled "L", "F", "U", etc., to rotate the cube in different directions.

## File Descriptions

- `bot.py`: Main file to run the Discord bot.
- `ui_setup.py`: Contains the UI setup for the bot, including button callbacks and embed creation.
- `manim_code.py`: Manim scenes for rendering the Rubik's Cube.
- `config.py`: Configuration file for storing the bot token and other settings.

## Notes

- Ensure that all necessary files such as `message_id.txt`, `fast_setting.txt`, `state.txt`, and `camera_orientation.txt` are present in the root directory as they are used for storing the bot's state and settings.

- The bot uses Manim to render the cube, so ensure that Manim is correctly installed and configured on your system.

## Troubleshooting

- If you encounter issues with rendering, ensure that Manim is properly installed and that your Python environment is correctly set up.
- Check the console for any error messages and ensure that all dependencies are installed.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
