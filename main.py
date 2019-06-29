from discord.ext import commands
import discord
from libs import macro


class Cogs:
    safe = [
        "cogs.imgflip",
        "cogs.misc",
        "cogs.nekobot"
    ]


bot = commands.Bot(command_prefix='m!')
bot.remove_command('help')

for cog in Cogs.safe:
    bot.load_extension(cog)


    def __init__(self, bot):
        self.bot = bot


@bot.event
async def on_command_error(ctx, error):
    if hasattr(ctx.command, 'on_error'):
        return

    ignored = commands.CommandNotFound

    error = getattr(error, 'original', error)

    if isinstance(error, ignored):
        print('ye')
        return

    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send(embed=await macro.error(str(error)))

    elif isinstance(error, AssertionError):
        await ctx.send(embed=await macro.error(f"{str(error).replace('AssertionError: ', '')}"))

    elif isinstance(error, commands.DisabledCommand):
        await ctx.send(f'{ctx.command} has been disabled.')

    elif isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send(embed=await macro.error(f"You forgot an argument!\n```{error}```"))
    else:
        await ctx.send(embed=await macro.error(
            f'Woah there partner. :cowboy: It seems as though you ran into a serious error. \nPlease contact @tedell#0001 and DM him the text below, along with the command you used, and how you typed it out.\n```{str(error)}```'))


@bot.event
async def on_ready():
    print(f"""READY\nUSER:{bot.user}\ngamer time :sunglasses:""")
    await bot.change_presence(activity=discord.Game(name='m!help || Use m!create to start an account!'),
                              status=discord.Status.idle)


bot.run('')
