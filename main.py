import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
jarp_token = os.getenv('DISCORD_TOKEN')

jarp_intents = discord.Intents.default()
jarp_intents.message_content = True
jarp_intents.members = True
jarp_intents.presences = True

jarp_handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
logging.basicConfig(level=logging.DEBUG, handlers=[jarp_handler])

jarp = commands.Bot(command_prefix='jarp ', intents=jarp_intents)

@jarp.event
async def on_ready():
    print("Ana JARP")
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py") and filename != "__init__.py":
            await jarp.load_extension(f"cogs.{filename[:-3]}")


jarp.run(jarp_token)