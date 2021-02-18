# Easter egg commands

# Setup
import random
from discord.ext import commands


# Check if message sender is me (owner of the script)
def is_author(ctx):
    with open("id.txt", 'r') as file:
        author_id = int(file.read())
    return author_id == ctx.author.id


class Ha(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Events: @commands.Cog.listener()
    # Commands: @commands.command()

    # Russian text message simulator
    @commands.command(hidden=True)
    @commands.check(is_author)
    async def russian(self, ctx):
        await ctx.send("Привет, меня зовут Дмитри)))))\n"
                       "Как твои дела?)))")

    # Pog reactor
    @commands.Cog.listener()
    async def on_message(self, message):

        # Checking if "pog" is in the message
        if "pog" in message.content.lower():
            await message.add_reaction(":pog:774317093834719263")

        # Checking if any of these communist/russia keywords are in the message
        if any(_ in message.content.lower() for _ in ["commie", "communist", "communism",
                                                      "russia", "soviet", "union", "россия",
                                                      "russophile", "cossack", "stalin", "ussr",
                                                      "lenin", "putin", "vladimir", "moscow", "siberia",
                                                      "gulag", "gopnik", "vodka", "slav", "khruschev"]):
            await message.add_reaction(":ussr:772506172611756072")

    # Auto show playlist reference
    @commands.command(hidden=True)
    @commands.check(is_author)
    async def playlist(self, ctx):

        # Storage and index
        playlist = [["Title", "Link"],
                    ["Oldies", "https://music.youtube.com/playlist?list=PLncUJ2gq6JxzyroJE6legsDW1iBT7TrTj"],
                    ["Back To School", "https://music.youtube.com/playlist?list=PLncUJ2gq6JxzGVaw4IXzlfUMn6TRvONKz"],
                    ["Not English", "https://music.youtube.com/playlist?list=PLncUJ2gq6JxxaJulekvb7s69yF94W6BqV"],
                    ["Хард Басс", "https://music.youtube.com/playlist?list=PLncUJ2gq6JxwDB1mEzf04YFsFDtaaeh9e"],
                    ["18 kiloWurtz", "https://music.youtube.com/playlist?list=PLncUJ2gq6JxyCKJIxzE1dD6RUqsn28bzW"]]

        guide = ""

        for title, link in playlist:

            gap = ""
            for _ in range(17 - len(title)):
                gap += " "

            line = f"{title}{gap} | {link}\n"
            guide += line

        await ctx.send(f"```{guide}```")

    # Downtime command for Abdul
    @commands.command(hidden=True)
    async def downtime(self, ctx):
        await ctx.send("Downtime is literally 0s; I'm up and running right now, дебил ты.")


# Add cog to main bot file
def setup(bot):
    bot.add_cog(Ha(bot))
