# Database module for bot

# Setup
import discord
from discord.ext import commands


class Database(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Events: @commands.Cog.listener()
    # Commands: @commands.command()

    # Record Ruby's Tutorial progress
    @commands.command()
    async def update_ruby(self, ctx, module: int, step: int):

        # Layout of modules and steps
        layout = [[1, 8], [2, 17],
                  [3, 15], [4, 15],
                  [5, 11], [6, 15],
                  [7, 17], [8, 7],
                  [9, 13], [10, 12],
                  [11, 7], [12, 10],
                  [13, 15], [14, 8],
                  [15, 10], [16, 4]]

        if not 0 < module <= 16:
            await ctx.send("Invalid module.")
            return
        else:
            if not 0 < step <= layout[module - 1][1]:
                await ctx.send("Invalid step.")
                return

        with open("../discordBot/data/ruby.txt", "r+") as ruby:

            # Recording data in a list
            data = []
            for line in ruby:
                data.append(line)

        # Replacing data
        index = 0
        data_exists = False
        for line in data:
            if str(ctx.author) in line:
                data[index] = f"{ctx.author} | {module}, {step}\n"
                data_exists = True
                break
            index += 1

        # Adding new line if the database doesn't already contain the user's info
        if not data_exists:
            data.append(f"{ctx.author} | {module}, {step}\n")

        # Writing to file
        with open("../discordBot/data/ruby.txt", "w") as ruby:
            for line in data:
                ruby.write(line)
        await ctx.send("Database updated!")

    # View Ruby's Tutorial Progress
    @commands.command()
    async def view_ruby(self, ctx):
        with open("../discordBot/data/ruby.txt", 'r') as ruby:
            await ctx.send(f"```{ruby.read()}```")


# Add cog to main bot file
def setup(bot):
    bot.add_cog(Database(bot))