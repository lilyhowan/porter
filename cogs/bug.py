import discord
from discord.ext import commands
import json, requests

class Bug(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bug_data = requests.get("https://acnhapi.com/v1/bugs/")

    @commands.command(name="bug", help="Returns information on specified bug")
    async def bug(self, ctx, *, bug_input):
        # convert all characters to lowercase and replace whitespace in string with underscore to match JSON data
        bug_input = bug_input.lower().replace(" ", "_")

        name = self.bug_data.json()[bug_input]["name"]["name-USen"].title()
        catch_phrase = self.bug_data.json()[bug_input]["catch-phrase"]
        price = self.bug_data.json()[bug_input]["price"]
        location = self.bug_data.json()[bug_input]["availability"]["location"]
        rarity = self.bug_data.json()[bug_input]["availability"]["rarity"]
        
        await ctx.send(f"***{name}***\n\"{catch_phrase}\" \
        \n**Selling price**: {price} bells\n**Location**: {location}\n**Rarity**: {rarity}")

def setup(bot):
    bot.add_cog(Bug(bot))