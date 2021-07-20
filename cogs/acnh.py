import discord
from discord.ext import commands
import json, urllib.request

class ACNH(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    '''@commands.Cog.listener()
    async def on_message(self, message):
        if self.bot.user.mentioned_in(message):
            if "test" in message.content:
                response = urllib.request.urlopen("http://acnhapi.com/v1/fish/60")
                fish_data = json.loads(response.read())
                await message.channel.send(fish_data["file-name"])
        await self.bot.process_commands(message)'''

    @commands.command(name="birthday2", help="Returns specified villager's birthday")
    async def speak(self, ctx, villager):
        response = urllib.request.urlopen(f"http://acnhapi.com/v1/villagers/")
        birthday_data = json.loads(response.read())
        await ctx.send(birthday_data)
        #await ctx.send(f"{birthday_data['name']['name-USen']}'s birthday is on {birthday_data['birthday-string']} ({birthday_data['birthday']}).")

    @commands.command(name="birthday", help="Returns specified villager's birthday")
    async def speak(self, ctx, villager):
        response = urllib.request.urlopen(f"http://acnhapi.com/v1/villagers/{villager}")
        birthday_data = json.loads(response.read())
        await ctx.send(f"{birthday_data['name']['name-USen']}'s birthday is on {birthday_data['birthday-string']} ({birthday_data['birthday']}).")

def setup(bot):
    bot.add_cog(ACNH(bot))