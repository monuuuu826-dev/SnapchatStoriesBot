import logging
from bot import Config
from pyrogram import Client, __version__
from pyrogram.raw.all import layer

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

plugins = dict(root="bot/modules")


class Bot(Client):

    def __init__(self):
        super().__init__(name="Nexiuo".39591986,
                         api_id=Config.,
                         api_hash=Config.867492ad46ef46ee807a7c62bdc372f4,
                         bot_token=Config.8482963758:AAG9XsJhAtz0MVxqRVMbOi1RZeaGhlSLRgs,
                         plugins=plugins)

    async def start(self):
        await super().start()
        me = await self.get_me()
        un = '@' + me.username
        LOGGER.info(
            f"Pyrogram v{__version__} (Layer {layer}) started on {un}.")

    async def stop(self, *args):
        await super().stop()
        LOGGER.info('Bot Stopped ! Bye..........')


if __name__ == "__main__":
    app = Bot()
    app.run()
