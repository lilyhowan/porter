import discord
from discord.ext import commands
import json, urllib.request

class Villager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="birthday", help="Returns specified villager's birthday")
    async def birthday(self, ctx, villager):
        try:
            response = urllib.request.urlopen(f"http://acnhapi.com/v1/villagers/")
            birthday_data = json.loads(response.read())
            villager = villager.capitalize()
            # find villager ID from given villager name
            for i in birthday_data:
                if villager in birthday_data[i]["name"].values():
                    villager_id = birthday_data[i]["id"]
                    break
            response = urllib.request.urlopen(f"http://acnhapi.com/v1/villagers/{villager_id}")
            villager_data = json.loads(response.read())
            await ctx.send(f"{villager_data['name']['name-USen']}'s birthday is on {villager_data['birthday-string']}.")
        except:
            await ctx.send("Specified villager could not be found.")

def setup(bot):
    bot.add_cog(Villager(bot))