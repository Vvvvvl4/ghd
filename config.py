## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgCmkWAqPeKAph4llVxjcNU2DQj7Ass0dNo0lYTcl2aHefPDYlNdV72UkqjsRMK7iXseOiH9uSB-7vIZcJjEBXl1AgycwZZUd3fTvVOBIUqhJKZu0Kavxj-RA8bwze3Q7okb0KRKXQF10RCgWa6sY0iHGFu7az3-fEH9pgfXOSE6smlHTMkjoWBt0RtMi7KJVaJfPdTJ4m2epay_KkuEYP5vdRx9YtGXGlsgYMq6suq64bcb3MfSqqbysW8J2qJuIdXeMQQfNcoC-siBr_cnTHP7eXRe6ff95pTq9JzRXtjIEJ1hF7YbZjQECk0RiPhT6Ye8jXlHmcISfZSpqYe9Iy8UfpDjDAA")
BOT_TOKEN = getenv("BOT_TOKEN", "5390190565:AAHBfSJIxkvO5WFF1EP8UrHoh7fcql_FAPo")
BOT_NAME = getenv("BOT_NAME", "MUSIC RANI")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "RANI")
OWNER_USERNAME = getenv("OWNER_USERNAME", "@Q4_NB")
ALIVE_NAME = getenv("ALIVE_NAME", "RANI")
BOT_USERNAME = getenv("BOT_USERNAME", "MUSIC_1Qbot")
OWNER_ID = getenv("OWNER_ID", "2123424524")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "@Q4_NB")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "RRNN44")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "RRNN44")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2123424524").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
