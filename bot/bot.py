import os
import random
import json, urllib.request

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix="~")

@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        if "test" in message.content:
            response = urllib.request.urlopen("http://acnhapi.com/v1/fish/60")
            fish_data = json.loads(response.read())
            await message.channel.send(fish_data["file-name"])
    await bot.process_commands(message)

@bot.command(name="birthday", help="Returns specified villager's birthday")
async def speak(ctx, villager):
    response = urllib.request.urlopen(f"http://acnhapi.com/v1/villagers/{villager}")
    birthday_data = json.loads(response.read())
    await ctx.send(f"{birthday_data['name']['name-USen']}'s birthday is on {birthday_data['birthday-string']} ({birthday_data['birthday']}).")

bot.run(TOKEN)