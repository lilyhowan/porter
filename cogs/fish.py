import json
import requests
import discord

from discord.ext import commands
from assets.creatures import creature_rarity


class Fish(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='fish', help='Returns information about the specified fish')
    async def fish(self, ctx, *, fish_name):
        # convert all characters to lowercase and replace whitespace in string with underscore to match JSON data
        fish_name = fish_name.lower().replace(' ', '_')

        # fetch fish data using specified fish_name
        fish = requests.get(f'https://acnhapi.com/v1/fish/{fish_name}').json()
        availability = fish["availability"]

        embed = discord.Embed(
            title=fish["name"]["name-USen"].title(),
            description=f'"{fish["museum-phrase"]}"')
        embed.set_thumbnail(url=f'http://acnhapi.com/v1/icons/fish/{fish_name}')

        embed.add_field(name='Details',
                        value=f'**Nook\'s Price**: {fish["price"]} bells\n '
                        f'**CJ\'s Price**: {fish["price-cj"]} bells\n '
                        f'**Rarity**: {creature_rarity[availability["rarity"]]}',
                        inline=True)
        
        if availability['isAllDay']:
            availability["time"] = 'All day'
        embed.add_field(name='Availability',
                        value=f'**Time**: {availability["time"]}\n '
                        f'**Location**: {availability["location"]}\n '
                        f'**Shadow**: {fish["shadow"]}',
                        inline=True)

        embed.set_footer(text=f'"{fish["catch-phrase"]}"')

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Fish(bot))
