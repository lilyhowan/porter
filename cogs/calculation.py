import discord
from discord.ext import commands

class Calculation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="add", help="Performs addition on given numbers (space separated)")
    async def add(self, ctx, *values):
        num_list = [int(i) for i in list(values)]
        await ctx.send(str(sum(num_list)))

def setup(bot):
    bot.add_cog(Calculation(bot))