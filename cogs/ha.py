# Easter egg commands

# Setup
import discord
from discord.ext import commands


# Author check
def is_author(ctx):
    with open("id.txt", 'r') as file:
        author_id = int(file.read())
    return author_id == ctx.author.id


class Ha(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Events: @commands.Cog.listener()

    # Commands: @commands.command()
    @commands.command(hidden=True)
    @commands.check(is_author)
    async def russian(self, ctx):
        await ctx.send("Привет, меня зовут Дмитри)))))"
                       "Как твои дела?)))")


# Add cog to main bot file
def setup(bot):
    bot.add_cog(Ha(bot))
