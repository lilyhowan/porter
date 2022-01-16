import json
import requests
import discord

from discord.ext import commands
from assets.villagers import villager_filenames

class Villager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='villager', help='Returns information about the specified villager')
    async def villager(self, ctx, *, villager_name):
        # the API data uses villager filenames as keys
        # to prevent potentially iterating over the entire set of villagers, the file assets/villagers.py
        # contains the name of every villager (in US english) and their respective filename within a dict
        villager_filename = villager_filenames[villager_name.lower()]

        # fetch villager data using specified villager_name
        villager = requests.get(f'http://acnhapi.com/v1/villagers/{villager_filename}').json()

        embed = discord.Embed(
            title=villager["name"]["name-USen"].title(),
            description=villager["catch-phrase"])
        embed.set_thumbnail(url=f'http://acnhapi.com/v1/icons/villagers/{villager_filename}')

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Villager(bot))
