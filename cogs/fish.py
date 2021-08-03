import discord
from discord.ext import commands
import json, requests

class Fish(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.fish_data = requests.get("https://acnhapi.com/v1/fish/")

    @commands.command(name="fish", help="Returns information on specified fish")
    async def fish(self, ctx, *, fish_input):
        # convert all characters to lowercase and replace whitespace in string with underscore to match JSON data
        fish_input = fish_input.lower().replace(" ", "_")

        name = self.fish_data.json()[fish_input]["name"]["name-USen"].title()
        catch_phrase = self.fish_data.json()[fish_input]["catch-phrase"]
        price = self.fish_data.json()[fish_input]["price"]
        location = self.fish_data.json()[fish_input]["availability"]["location"]
        rarity = self.fish_data.json()[fish_input]["availability"]["rarity"]
        
        await ctx.send(f"***{name}***\n\"{catch_phrase}\" \
        \n**Selling price**: {price} bells\n**Location**: {location}\n**Rarity**: {rarity}")

def setup(bot):
    bot.add_cog(Fish(bot))