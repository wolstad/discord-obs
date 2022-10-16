import asyncio
from config import Config
from discord.bot import Bot
from obs import OBS

config = Config()
obs = OBS()
bot = Bot()

async def start():
    # Create Config
    config.initialize()

    # Connect OBS
    await obs.create(config.get_ip(), config.get_port(), config.get_password(), config.get_browser_source())
    await obs.connect()

    # Connect bot
    await bot.create(config, obs)
    await bot.connect_bot()

asyncio.run(start())