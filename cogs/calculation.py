import discord
from discord.ext import commands

class Calculation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="add", help="Performs addition on given numbers (space separated)")
    async def add(self, ctx, *values):
        num_list = [int(i) for i in list(values)]
        await ctx.send(str(sum(num_list)))

    @commands.command(name="sub", help="Performs subtraction on given numbers (space separated)")
    async def sub(self, ctx, *values):
        num_list = [int(i) for i in list(values)]
        value = num_list[0]
        for num in num_list[1:]:
            value -= num
        await ctx.send(str(value))

def setup(bot):
    bot.add_cog(Calculation(bot))