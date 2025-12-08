from discord.ext import commands

class OnMessage(commands.Cog):
    def __init__(self, jarp):
        self.jarp = jarp

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.jarp.user:
            return

        pass # empty for now



async def setup(jarp):
    await jarp.add_cog(OnMessage(jarp))

