import discord
from discord.ext import commands
import json, requests

class Bug(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bug_data = requests.get("https://acnhapi.com/v1/bugs/").json()

    @commands.command(name="bug", help="Returns information on specified fish")
    async def bug(self, ctx, *, bug_name):
        creature_rarity = {'Common': '★', 'Uncommon': '★★', 'Rare': '★★★', 'Ultra-rare': '★★★★'}

        # convert all characters to lowercase and replace whitespace in string with underscore to match JSON data
        bug_name = bug_name.lower().replace(' ', '_')
        bug = self.bug_data[bug_name]
        availability = bug['availability']

        embed=discord.Embed(title=bug['name']['name-USen'].title(), description=f"\"{bug['museum-phrase']}\"")
        embed.set_thumbnail(url='http://acnhapi.com/v1/icons/bugs/' + bug_name)

        embed.add_field(name='Details',
                        value=f"**Nook's Price**: {bug['price']} bells\n "
                        f"**Flick's Price**: {bug['price-flick']} bells\n"
                        f"**Rarity**: {creature_rarity[availability['rarity']]}",
                        inline=True)
        embed.set_footer(text=f"\"{bug['catch-phrase']}\"")

        if availability['isAllDay']:
            availability['time'] = 'All day'

        embed.add_field(name='Availability',
                        value=f"**Time**: {availability['time']}\n "
                        f"**Location**: {availability['location']}\n",
                        inline=True)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Bug(bot))