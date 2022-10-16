import discord
import config
import obs
from discord.ext import commands

class MediaGrabber(commands.Cog, name='Media Grabber'):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("MediaGrabber loaded.")

    # Check all messages for images
    @commands.Cog.listener("on_message")
    async def img_display(self, message):
        # Check if in image channel
        if message.channel.id == config.get_image_channel() and message.attachments:
            await obs.img_toggle(message.attachments[0].url)

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


async def setup(bot):
    await bot.add_cog(MediaGrabber(bot))