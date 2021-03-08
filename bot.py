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


'''@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        if "speak" in message.content:
            await message.channel.send(random.choice(babys_first_words))
        if "sit" in message.content:
            await message.channel.send("<:bab:809691932779216936>")
    if message.content == ":3":
        response = ">:3"
        await message.channel.send(response)
    await bot.process_commands(message)'''

@bot.command(name="birthday", help="Returns specified villager's birthday")
async def speak(ctx, villager):
    response = urllib.request.urlopen(f"http://acnhapi.com/v1/villagers/{villager}")
    birthday_data = json.loads(response.read())
    await ctx.send(f"{birthday_data['name']['name-USen']}'s birthday is on {birthday_data['birthday-string']} ({birthday_data['birthday']}).")

bot.run(TOKEN)
#error handling, file output https://realpython.com/how-to-make-a-discord-bot-python/#creating-a-discord-connection