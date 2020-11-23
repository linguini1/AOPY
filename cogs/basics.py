# Basic commands

# Setup
import datetime
import math
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
        await ctx.channel.purge(limit=amount + 1)

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
            uptime = datetime.datetime.now() - boot
            hours = uptime.seconds / (60 * 60)
            minutes = math.floor(((hours - math.floor(hours)) * 60) - (uptime.seconds % 60) / 60)
        await ctx.send(f"Uptime is {math.floor(hours)}hr, "
                       f"{minutes}min, "
                       f"{uptime.seconds % 60}s.")


# Add cog to main bot file
def setup(bot):
    bot.add_cog(Basics(bot))
