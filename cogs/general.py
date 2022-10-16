import discord
import traceback
from discord.ext import commands

class General(commands.Cog, name='General'):
    def __init__(self, bot, config):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("General loaded.")


    # Command error handling
    @commands.Cog.listener()
    async def on_command_error(ctx, error):
        await ctx.message.delete()
        await ctx.message.author.send("[Error] Invalid command or syntax. Use '.help' for assistance.")
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
            