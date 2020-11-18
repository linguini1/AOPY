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
        await ctx.send("Привет, меня зовут Дмитри)))))\n"
                       "Как твои дела?)))")

    @commands.Cog.listener()
    async def on_message(self, message):
        if "pog" in message.content.lower() or "poggers" in message.content.lower():
            await message.add_reaction(":pog:774317093834719263")


# Add cog to main bot file
def setup(bot):
    bot.add_cog(Ha(bot))
