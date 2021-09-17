import discord
from discord.ext import commands
import json, requests

class Fish(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.fish_data = requests.get('https://acnhapi.com/v1/fish/').json()

   
    @commands.command(name='fish', help='Returns information on specified fish')
    async def fish(self, ctx, *, fish_name):
        creature_rarity = {'Common': '★', 'Uncommon': '★★', 'Rare': '★★★', 'Ultra-rare': '★★★★'}

        # convert all characters to lowercase and replace whitespace in string with underscore to match JSON data
        fish_name = fish_name.lower().replace(' ', '_')
        fish = self.fish_data[fish_name]
        availability = fish['availability']
        
        embed=discord.Embed(title=fish['name']['name-USen'].title(), description=f"\"{fish['museum-phrase']}\"")
        embed.set_thumbnail(url='http://acnhapi.com/v1/icons/fish/' + fish_name)

        embed.add_field(name='Details',
                        value=f"**Nook's Price**: {fish['price']} bells\n "
                        f"**CJ's Price**: {fish['price-cj']} bells\n "
                        f"**Rarity**: {creature_rarity[availability['rarity']]}",
                        inline=True)
        embed.set_footer(text=f"\"{fish['catch-phrase']}\"")

        if availability['isAllDay']:
            availability['time'] = 'All day'

        embed.add_field(name='Availability',
                        value=f"**Time**: {availability['time']}\n "
                        f"**Location**: {availability['location']}\n "
                        f"**Shadow**: {fish['shadow']}",
                        inline=True)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Fish(bot))