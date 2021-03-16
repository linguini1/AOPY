# Basic, core commands for general use cases

# Setup
import datetime
import math
import random
from discord.ext import commands, tasks

# Paths
startTime = "../AOPY/data/startTime.txt"

# Channels
announcements = 755174545886937221

# Roles
everyone = 649243272501264404


class Basics(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.meeting.start()

    # Events: @commands.Cog.listener()
    # Commands: @commands.command()
    # Tasks: @tasks.loop()

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

    # Announce meetings_
    @tasks.loop(hours=1)
    async def meeting(self):

        # Remarks
        remarks = ["Be there or be square!",
                   "You better make it! :)"
                   "Don't be late!",
                   "Hope to see you there!",
                   "Bring your thinking cap.",
                   "BYOP!",
                   "Last one to join is a missing semicolon!",
                   "Last one to join is a broken webhook!",
                   "Don't forget to brush your teeth!",
                   "Make sure your text editor is up to date!",
                   "Dress code: semi-gamer."]

        # Wait until bot is ready
        await self.bot.wait_until_ready()

        # Important variables
        day = datetime.datetime.today().weekday()  # Current day
        currentTime = datetime.datetime.today().time()
        channel = self.bot.get_channel(announcements)  # Announcements channel
        everyonePing = channel.guild.default_role  # @everyone role

        # Between 3:00 and 4:00
        if datetime.time(15) < currentTime < datetime.time(16):

            # Meeting today
            if day == 1 or day == 5:
                await channel.send(f"{everyonePing}; Meeting today at 4:00PM! "
                                   f"{random.choice(remarks)}")

            # Meeting tomorrow
            elif day == 0 or day == 4:
                await channel.send(f"{everyonePing}; Meeting tomorrow at 4:00PM! "
                                   f"{random.choice(remarks)}")


# Add cog to main bot file
def setup(bot):
    bot.add_cog(Basics(bot))
