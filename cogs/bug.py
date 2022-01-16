import json
import requests
import discord

from discord.ext import commands
from assets.creatures import creature_rarity


class Bug(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="bug", help="Returns information about the specified bug")
    async def bug(self, ctx, *, bug_name):
        # convert all characters to lowercase and replace whitespace in string with underscore to match JSON data
        bug_name = bug_name.lower().replace(' ', '_')

        # fetch bug data using specified bug_name
        bug = requests.get(f'https://acnhapi.com/v1/bugs/{bug_name}').json()
        availability = bug["availability"]

        embed = discord.Embed(
            title=bug["name"]["name-USen"].title(), description=f'"{bug["museum-phrase"]}"')

        embed.add_field(name='Details',
                        value=f'**Nook\'s Price**: {bug["price"]} bells\n '
                        f'**Flick\'s Price**: {bug["price-flick"]} bells\n '
                        f'**Rarity**: {creature_rarity[availability["rarity"]]}',
                        inline=True)

        if availability["isAllDay"]:
            availability["time"] = "All day"
        embed.add_field(name='Availability',
                        value=f'**Time**: {availability["time"]}\n '
                        f'**Location**: {availability["location"]}\n',
                        inline=True)

        embed.set_thumbnail(url=bug["icon_uri"])
        embed.set_footer(text=f'"{bug["catch-phrase"]}"')

        await ctx.send(embed=embed)

    @bug.error
    async def bug_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('A bug name is required.')
        else:
            await ctx.send('Bug not found.')


def setup(bot):
    bot.add_cog(Bug(bot))
