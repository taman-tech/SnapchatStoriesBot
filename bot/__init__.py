import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("11496461"))
    API_HASH = os.environ.get("ab52f38fc71b58e707bf9e9aef4c9963")
    BOT_TOKEN = os.environ.get("5632952116:AAHeZw2x4FeizqyPJaAwY-SiMemoCjuLTXU")
    BOT_USERNAME = os.environ.get("snapchatbytamanbot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
