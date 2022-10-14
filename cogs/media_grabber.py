import discord
from discord.ext import commands

class MediaGrabber(commands.Cog, name='Media Grabber'):
    def __init__(self, bot):
        self.bot = bot