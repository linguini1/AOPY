# Discord bot file

# Setup
import discord
import datetime
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='.')
with open("token.txt", 'r') as file:
    token = file.read()

# Channels
aopyLog = 778379334284607518

# Paths
startTime = "../AOPY/data/startTime.txt"


# Author check
def is_author(ctx):
    with open("id.txt", 'r') as file:
        author_id = int(file.read())
    return author_id == ctx.author.id


# Load function
@bot.command()
@commands.check(is_author)
async def load(ctx, extension):
    try:
        bot.load_extension(f"cogs.{extension}")
        await ctx.send(f"{extension} has been loaded.")
        await bot.get_channel(aopyLog).send(f"{ctx.author} just loaded `{extension}`")
    except discord.ext.commands.errors.ExtensionNotFound:
        await ctx.send(f"{extension} does not exist.")
    except discord.ext.commands.errors.ExtensionAlreadyLoaded:
        await ctx.send(f"{extension} has already been loaded.")


# Unload function
@bot.command()
@commands.check(is_author)
async def unload(ctx, extension):
    try:
        bot.unload_extension(f"cogs.{extension}")
        await ctx.send(f"{extension} has been unloaded.")
        await bot.get_channel(aopyLog).send(f"{ctx.author} just unloaded `{extension}`")
    except discord.ext.commands.errors.ExtensionNotFound:
        await ctx.send(f"{extension} does not exist.")
    except discord.ext.commands.errors.ExtensionNotLoaded:
        await ctx.send(f"{extension} is not loaded.")


# Reload function (to refresh cogs with changes)
@bot.command()
@commands.check(is_author)
async def reload(ctx, extension):
    try:
        bot.unload_extension(f"cogs.{extension}")
        bot.load_extension(f"cogs.{extension}")
        await ctx.send(f"{extension} has been reloaded. Your changes should be up to date.")
        await bot.get_channel(aopyLog).send(f"{ctx.author} just reloaded `{extension}`")
    except discord.ext.commands.errors.ExtensionNotLoaded:
        await ctx.send(f"{extension} needs to be loaded first, or does not exist.")


# Error catching
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("That command doesn't exist, друг.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You're missing an argument.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("One or more of your arguments were not of the required type.")
    elif isinstance(error, commands.MissingRole):
        await ctx.send("You don't have permission to use this command.")
    elif isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have permission to use this command.")
    else:
        print(f"{error} | Type: {error.__class__}")
        await bot.get_channel(aopyLog).send(f"{error}\nCog: `{ctx.cog.qualified_name}`"
                                            f"\nType: `{error.__class__}`"
                                            f"\nCommand: `{ctx.command.name}`"
                                            f"\nMessage was: ```{ctx.message.content}```")


# Loading all cogs on start
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


# Booting
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Potato Fields"))
    with open(startTime, 'w') as boot:
        dt = datetime.datetime.now()
        boot.write(f"{dt.year}-{dt.month}-{dt.day}-{dt.hour}-{dt.minute}-{dt.second}")
    print("Bot is online, baby!")
    log = bot.get_channel(aopyLog)
    await log.send("Bot is online, baby!")


# Running
bot.run(token)
