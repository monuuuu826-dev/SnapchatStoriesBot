import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "39591986"))
    API_HASH = os.environ.get("API_HASH", "867492ad46ef46ee807a7c62bdc372f4")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8482963758:AAG9XsJhAtz0MVxqRVMbOi1RZeaGhlSLRgs")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@Monuuu01") 
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
