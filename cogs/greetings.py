from discord.ext import commands

class Greetings(commands.Cog):
    def __init__(self, jarp):
        self.jarp = jarp

    @commands.command()
    async def greetings(self, priop, flso=None):
        FLSO = ['--help', '--hello', '-h', '--goodbye', '--bye', '-g', '-b']
        FLSO_hi = ['--hello', '-h']
        FLSO_bye = ['--bye', '--goodbye', '-b', '-g']
        help_message = ("Allowed First Level Secondary Operations for the Primary Operation greetings: --hello/-h; --goodbye/--bye/-g/-b.\n"
                        "***(ex: jarp greetings --hello)***")
        help_string = "(Try: jarp greetings --help)"

        # user should enter: jarp greetings flso where flso is an element of FLSO

        if not flso:
            await priop.send(f"Please enter a First level Secondary Operation for the Primary operation greetings. {help_string}")
            return
        if flso not in FLSO:
            await priop.send(f"Please enter a valid First Level Secondary Operation for the Primary Operation greetings. {help_string}")
            return
        if flso in FLSO_hi:
            await priop.send(f"Hello, {priop.author.mention}!")
            return
        if flso in FLSO_bye:
            await priop.send(f"Goodbye, {priop.author.mention}!")
            return
        if flso in ['--help']:
            await priop.send(help_message)

async def setup(jarp):
    await jarp.add_cog(Greetings(jarp))