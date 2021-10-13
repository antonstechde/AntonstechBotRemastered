import pathlib

from discord import Client, Intents, Embed
from discord.ext.commands import Bot
from discord_slash import SlashCommand, SlashContext
from utils import utils
from utils import config
import os

# Note that command_prefix is a required but essentially unused paramater.
# Setting help_command=False ensures that discord.py does not create a !help command.
# Enabling self_bot ensures that the bot does not try and parse messages that start with "!".
bot = Bot(command_prefix="!", self_bot=True, intents=Intents.default())
bot.remove_command("help")

slash = SlashCommand(bot, sync_commands=True)

utils.run_checks()

for file in os.listdir(utils.get_project_dir() + "/cogs/"):
    if os.path.isdir(utils.get_project_dir() + "/cogs/" + file):
        continue

    bot.load_extension(f"cogs.{file[:-3]}")


bot.run(utils.CONFIG.TOKEN)
