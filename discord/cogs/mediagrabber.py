import discord
from discord.ext import commands

class MediaGrabber(commands.Cog, name='Media Grabber'):
    def __init__(self, bot, config, obs):
        self.bot = bot
        self.config = config
        self.obs = obs

    @commands.Cog.listener()
    async def on_ready(self):
        print("MediaGrabber loaded.")

    ##################
    # Media Commands #
    ##################

    # Clear the browser source
    @commands.command()
    async def clear_browser(self, ctx):
        if ctx.message.channel.id == self.config.get_image_channel():
            if await self.obs.clear_browser_source():
                await ctx.message.channel.send(f":white_check_mark: Successfully cleared browser source.")
            else:
                raise commands.CommandError("Failed to clear browser source")
        await ctx.message.delete()

    # Display an image on screen
    @commands.command()
    async def img(self, ctx, time=15):
        # Check if in image channel and exactly one attachment
        if ctx.message.channel.id == self.config.get_image_channel() and len(ctx.message.attachments) == 1:
            if self.obs.get_browser_status():
                raise commands.CommandError("Browser source in use")
            await ctx.message.channel.send(f":white_check_mark: Attempting to display image for {time} seconds.")
            await self.obs.img_trigger(ctx.message.attachments[0].url, int(time))
            await ctx.message.delete()
        else:
            raise commands.CommandError("Usage: .img <time>. You must also include exactly one image attachment")


    ##################
    # Admin Commands #
    ##################

    # Define image channel
    @commands.command()
    async def mg_set_channel(self, ctx):
        member = ctx.message.author
        channel = ctx.message.channel
        self.config.set_image_channel(channel)
        await member.send(':white_check_mark: Updated image channel.')
        await ctx.message.delete()