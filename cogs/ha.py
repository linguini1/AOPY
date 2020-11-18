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

    # Russian text message simulator
    @commands.command(hidden=True)
    @commands.check(is_author)
    async def russian(self, ctx):
        await ctx.send("Привет, меня зовут Дмитри)))))\n"
                       "Как твои дела?)))")

    # Pog reactor
    @commands.Cog.listener()
    async def on_message(self, message):
        if "pog" in message.content.lower() or "poggers" in message.content.lower():
            await message.add_reaction(":pog:774317093834719263")

    # Auto playlist
    @commands.command(hidden=True)
    @commands.check(is_author)
    async def playlist(self, ctx):

        # Storage and index
        playlist = [["Веснушки", "https://www.youtube.com/watch?v=prPZUmsbpS8"],
                    ["Аленка", "https://www.youtube.com/watch?v=zJyl_BF6L-4"],
                    ["Да Да Да", "https://www.youtube.com/watch?v=gQDmNv86cYw"],
                    ["Мама мы все сощли с ума", "https://www.youtube.com/watch?v=jVlwtapN0yc"],
                    ["Когда твоя девушка больна", "https://www.youtube.com/watch?v=X1TyisQ1bNk"],
                    ["Группа крови", "https://www.youtube.com/watch?v=xtxjm7ciwmc&t=33s"],
                    ["Троллейбус", "https://www.youtube.com/watch?v=eS7ow489tvU"],
                    ["Место для шага вперед", "https://www.youtube.com/watch?v=3MWofo1ohY0"],
                    ["Вкино", "https://www.youtube.com/watch?v=ODUUR-r3z-k"],
                    ["Без тебя нельзя", "https://www.youtube.com/watch?v=134vj4I4Lfc"],
                    ["Одуванчик", "https://www.youtube.com/watch?v=vqCt-WEA3Fg"],
                    ["Искры", "https://www.youtube.com/watch?v=95PhFfV1I8U"],
                    ["Поболело и прошло", "https://www.youtube.com/watch?v=RMD60YUisxk"],
                    ["Tas la Touche Manouche", "https://www.youtube.com/watch?v=Aaak_SvPQds"],
                    ["Fibre de Verre", "https://www.youtube.com/watch?v=XLtvaQMJMGw"],
                    ["Moi Mon Ame et Ma Conscience", "https://www.youtube.com/watch?v=_obZoNHCaI8"],
                    ["Le shift", "https://www.youtube.com/watch?v=nIERsZXXZIw"],
                    ["Ca ira", "https://www.youtube.com/watch?v=SbEIjUrPXWk"],
                    ["99 Luftballons", "https://www.youtube.com/watch?v=hIIVK0NgK38"],
                    ["лбтд", "https://www.youtube.com/watch?v=HhkgVZfls_E"]]

        # Joining vc
        vc = ctx.author.voice.channel
        await vc.connect()

        # Sending commands
        for song in playlist:
            await ctx.send(f"-p {song[1]}")


# Add cog to main bot file
def setup(bot):
    bot.add_cog(Ha(bot))
