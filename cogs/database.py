# Database module for bot

# Setup
from discord.ext import commands


# Paths
rubyPath = "../AOPY/data/ruby.txt"
respPath = "../AOPY/data/responsibilities.txt"


class Database(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    """Events: @commands.Cog.listener()
    Commands: @commands.command()"""

    # Record Ruby's Tutorial progress
    @commands.command()
    @commands.has_role("Programmer")
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

        # Making sure the module isn't lower than 0 or higher than 16
        if not 0 < module <= 16:
            await ctx.send("Invalid module.")
            return

        # Making sure the step isn't lower than 0 or more than the number of steps in the specific module
        else:
            if not 0 < step <= layout[module - 1][1]:
                await ctx.send("Invalid step.")
                return

        with open(rubyPath, "r+") as ruby:

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
        with open(rubyPath, "w") as ruby:
            for line in data:
                ruby.write(line)
        await ctx.send("Database updated!")

    # View Ruby's Tutorial Progress
    @commands.command()
    async def view_ruby(self, ctx):
        with open(rubyPath, 'r') as ruby:
            await ctx.send(f"```{ruby.read()}```")

    # Record responsibilities
    @commands.command()
    async def update_resp(self, ctx, resp: str):

        # Sorting roles
        roles = []
        for role in ctx.author.roles:
            if "Programmer" in role.name:
                roles.append("Programmer")
            if "2D Artist" in role.name:
                roles.append("2D Artist")
            if "3D Artist" in role.name:
                roles.append("3D Artist")
            if "Musician" in role.name:
                roles.append("Musician")

        # Checking to make sure user used quotation marks
        if len(resp.split(" ")) < 2:
            await ctx.send("You probably forgot to put quotes around your responsibility, or it's too short!\n"
                           """Try writing `.update_resp "example responsibility"`""")
            return

        with open(respPath) as responsibilities:
            # Recording data in a list
            data = []
            for line in responsibilities:
                data.append(line)

        # Replacing data
        index = 0
        data_exists = False
        for line in data:
            if str(ctx.author) in line:
                data[index] = f"{ctx.author} | {[role for role in roles]} | {resp}\n"  # Format for data input
                data_exists = True
                break
            index += 1

        # Adding new line if the database doesn't already contain the user's info
        if not data_exists:
            data.append(f"{ctx.author} | {[role for role in roles]} | {resp}\n")

        # Writing to file
        with open(respPath, "w") as responsibilities:
            for line in data:
                responsibilities.write(line)
        await ctx.send("Database updated!")

    # View responsibilities
    @commands.command()
    async def view_resp(self, ctx):
        with open(respPath, 'r') as responsibilities:
            await ctx.send(f"```{responsibilities.read()}```")


# Add cog to main bot file
def setup(bot):
    bot.add_cog(Database(bot))
