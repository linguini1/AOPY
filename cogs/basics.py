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
        # Setting amount equal to 99 because otherwise it messes with Discord or something
        if amount > 99:
            amount = 99
        await ctx.channel.purge(limit=amount + 1)  # Added one to include the command message itself

    # Ping command
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Latency is {round(self.bot.latency * 1000)}ms.")

    # Uptime
    @commands.command()
    async def uptime(self, ctx, value="default"):
        with open(startTime, 'r') as start:
            s = start.read().split('-')

            # Creating a datetime object from the start date
            boot = datetime.datetime(int(s[0]), int(s[1]), int(s[2]), int(s[3]), int(s[4]))

            # Saving the difference in time between boot and now to uptime
            uptime = datetime.datetime.now() - boot
            hours = uptime.seconds / 3600 + uptime.days * 24
            minutes = (uptime.seconds / 60) % 60

        # Default return format
        if value == "default":
            await ctx.send(f"Uptime is {math.floor(hours)}hr, "
                           f"{math.floor(minutes)}min, "
                           f"{uptime.seconds % 60}s.")

        # Gives time including days
        elif value == "days":
            await ctx.send(f"Uptime is {uptime.days}d, "
                           f"{math.floor(hours) - uptime.days * 24}hr, "
                           f"{math.floor(minutes)}min, "
                           f"{uptime.seconds % 60}s.")

        # Gives time in minutes and seconds
        elif value == "minutes":
            await ctx.send(f"Uptime is {math.floor(minutes) + math.floor(hours) * 60}min, "
                           f"{uptime.seconds % 60}s.")

        # Gives time in seconds
        elif value == "seconds":
            await ctx.send(f"Uptime is {uptime.seconds + uptime.days * 24 * 60 * 60}s.")

        # Deals with incorrect input
        else:
            await ctx.send("You didn't give a valid format, дурак.")


# Add cog to main bot file
def setup(bot):
    bot.add_cog(Basics(bot))
