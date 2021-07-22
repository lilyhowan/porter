import discord
from discord.ext import commands
import json, urllib.request

class ACNH(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="birthday", help="Returns specified villager's birthday")
    async def birthday(self, ctx, villager):
        response = urllib.request.urlopen(f"http://acnhapi.com/v1/villagers/")
        birthday_data = json.loads(response.read())
        villager = villager.capitalize()

        for i in birthday_data:
            if villager in birthday_data[i]["name"].values():
                villager_id = birthday_data[i]["id"]
        
        response = urllib.request.urlopen(f"http://acnhapi.com/v1/villagers/{villager_id}")
        villager_data = json.loads(response.read())
        await ctx.send(f"{villager_data['name']['name-USen']}'s birthday is on {villager_data['birthday-string']} ({villager_data['birthday']}).")

def setup(bot):
    bot.add_cog(ACNH(bot))