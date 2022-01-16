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
            description=f'{villager["personality"]} {villager["species"]} ({villager["gender"]})')
        
        embed.set_thumbnail(url=villager["icon_uri"])
        embed.set_footer(text=f'"{villager["catch-phrase"]}"')


        await ctx.send(embed=embed)

    @villager.error
    async def villager_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('A villager name is required.')
        else:
            await ctx.send('Villager not found.')

def setup(bot):
    bot.add_cog(Villager(bot))
