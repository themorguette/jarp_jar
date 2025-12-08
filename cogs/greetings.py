from discord.ext import commands

class Greetings(commands.Cog):
    def __init__(self, jarp):
        self.jarp = jarp

    @commands.group()
    async def greetings(self, priop):
        if not priop.invoked_subcommand:
            await priop.send(f"Please enter a First Level Secondary Operation. Try jarp greetings --help for the list of possible FLSOs.")
            return

    @greetings.command(name='--hello')
    async def greetings_hello(self, flso):
        await flso.send(f"Hello, {flso.author.mention}!")
        return

    @greetings.command(name='--goodbye', aliases=['--bye'])
    async def greetings_goodbye(self, flso):
        await flso.send(f"Goodbye, {flso.author.mention}!")
        return

async def setup(jarp):
    await jarp.add_cog(Greetings(jarp))