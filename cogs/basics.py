# Basic commands

# Setup
import discord
from discord.ext import commands


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


# Add cog to main bot file
def setup(bot):
    bot.add_cog(Basics(bot))
