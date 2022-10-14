import discord
import config
from discord.ext import commands

class MediaGrabber(commands.Cog, name='Media Grabber'):
    def __init__(self, bot):
        self.bot = bot

    # Check all messages for images
    @commands.cog.listener
    async def on_message(message):
        # Check if in image channel
        if message.channel.id == config.get_image_channel():
            # Message contains an image
            if message.attachement:
                await message.channel.send(content=message.attachments[0].url)


    ##################
    # Admin Commands #
    ##################

    # Define image channel
    @commands.command()
    async def mg_set_channel(self, ctx):
        member = ctx.message.author
        channel = ctx.message.channel
        config.set_image_channel(channel)
        await member.send('[Success] Updated image channel.')
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(MediaGrabber(bot))