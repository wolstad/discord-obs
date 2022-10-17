import discord
import traceback
from discord.ext import commands

class General(commands.Cog, name='General'):
    def __init__(self, bot, config):
        self.bot = bot
        self.config = config
        self.error_prefix = ':x:'

    @commands.Cog.listener()
    async def on_ready(self):
        print("General loaded.")

    # Command error handling
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.message.delete() # Delete any invalid commands

        # Send an error message
        await ctx.message.channel.send(f"{self.error_prefix} {error}.")
            