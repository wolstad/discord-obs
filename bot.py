import discord
import config
import traceback
import sys
from discord.ext import commands
from discord import Status

###########################
# Setup Bot Configuration #
###########################

# Create a config if it does not yet exist
config.initialize()

TOKEN = config.get_token()
COMMAND_PREFIX = config.get_command_prefix()

# Define Intents
intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(command_prefix=COMMAND_PREFIX, intents=intents)

# Define bot extensions
extensions = []


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


# Load available cogs and extensions
if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension,error))
    bot.run(TOKEN)