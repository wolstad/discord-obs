import asyncio
from config import Config
from discord.bot import Bot
from obs import OBS

config = Config()
obs = OBS()
discord_bot = Bot()

async def start():
    # Create Config
    config.initialize()

    # Connect OBS
    await obs.create(config.get_ip(), config.get_port(), config.get_password(), config.get_browser_source())
    await obs.connect()

    # Connect bot
    await discord_bot.create(config, obs)
    await discord_bot.connect_bot()

asyncio.run(start())
