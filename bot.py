import discord
import config
import traceback
import sys
import asyncio
import frontend
from discord.ext import commands
from discord import Status

###########################
# Setup Bot Configuration #
###########################

# Create a config if it does not yet exist
config.initialize()

TOKEN = config.get_token()
COMMAND_PREFIX = config.get_command_prefix()

# Define bot extensions
extensions = ['cogs.mediagrabber']

# Define Intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)

###############
# Bot Events #
###############

# Log in
@bot.event
async def on_ready():
    print('Logged in as: ' + bot.user.name + ' (' + str(bot.user.id) + ')')
    print('------')


# Command error handling
@bot.event
async def on_command_error(ctx, error):
    await ctx.message.delete()
    await ctx.message.author.send("[Error] Invalid command or syntax. Use '.help' for assistance.")
    print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
    traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

#################
# Start Process #
#################

# Load cogs
async def load():
    for extension in extensions:
        try:
            await bot.load_extension(extension)
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension,error))

# Start bot
async def main():
    frontend.page.run()
    await load()
    await bot.start(TOKEN)

asyncio.run(main())