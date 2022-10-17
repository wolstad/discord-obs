import discord
from discord.cogs.mediagrabber import MediaGrabber
from discord.cogs.general import General
from discord.cogs.help import Help
from discord.ext import commands

class Bot():
    @classmethod
    async def create(self, config, obs, intents = discord.Intents.default()):
        self.config = config
        self.intents = intents
        self.obs = obs

        # Define bot
        self.intents.message_content = True
        self.bot = commands.Bot(command_prefix= self.config.get_command_prefix(), intents=intents)

        # Remove default help command
        self.bot.remove_command('help')

        return self

    async def load_cogs(self):
        print("Loading Cogs.")
        await self.bot.add_cog(General(self.bot, self.config))
        await self.bot.add_cog(MediaGrabber(self.bot, self.config, self.obs))
        await self.bot.add_cog(Help(self.bot))

    async def connect_bot(self):
        await self.load_cogs()
        print("Attempting to start Discord bot.")
        await self.bot.start(self.config.get_token())
