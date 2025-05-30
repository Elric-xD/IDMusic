import importlib
import asyncio
from pytgcalls import idle

from startup import LOGGER
from startup.plugins import ALL_MODULES
from startup import app, call

loop = asyncio.get_event_loop()


async def init():

    await app.start()
    LOGGER("MusicBot").info("Starting Music Bot!")

    for all_module in ALL_MODULES:
        importlib.import_module("startup.plugins" + all_module)

    LOGGER("MusicBot.plugins").info("Successfully Imported Modules")
    await call.start()
    LOGGER("MusicBot").info("Successfully Started Bot")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("MusicBot").info("Stopping Music Bot!")
