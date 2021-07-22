import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
bot = commands.Bot(command_prefix = "p!")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        # splicing to remove .py file extension
        bot.load_extension(f"cogs.{filename[:-3]}")

@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")

bot.run(os.getenv("DISCORD_TOKEN"))