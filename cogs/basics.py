# Basic commands

# Setup
import discord
import datetime
from discord.ext import commands

# Paths
startTime = "../AOPY/data/startTime.txt"


class Basics(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Events: @commands.Cog.listener()
    # Commands: @commands.command()

    # Clear command
    @commands.command()
    @commands.has_role("Mod")
    async def clear(self, ctx, amount: int):
        if amount > 99:
            amount = 99
        try:
            await ctx.channel.purge(limit=amount + 1)
        except discord.ext.commands.errors.MissingRequiredArgument:
            await ctx.send("You didn't specify how many messages to clear.")

    # Ping command
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Latency is {round(self.bot.latency * 1000)}ms.")

    # Uptime
    @commands.command()
    async def uptime(self, ctx):
        with open(startTime, 'r') as start:
            s = start.read().split('-')
            boot = datetime.datetime(int(s[0]), int(s[1]), int(s[2]), int(s[3]), int(s[4]))
        await ctx.send(f"Uptime is {datetime.datetime.now() - boot}.")


# Add cog to main bot file
def setup(bot):
    bot.add_cog(Basics(bot))
