## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME"AgAlEhtYSlYE0N2hwxvutJayYOQhHiCorawCvjP8AABco0Q86h2bjf5f0ro90jRjaVLQhfK-y3fT_GIvReg_kQyn27oGAJkBjvJI4HDSUgmD4d0hANldydNe9wYNt8H1Ag6m3gwypgYPgw9Y3-FDP4oI-TZq9U6AUcAstt6bmF5k0GToMZpvzdtOYv5vyuwrmpfkCDHvOv83csDKtwrI4Z-NkjDbpdphxr9OS2l57yY-n0U3vFG0aDXkBT5_iqIvFLX1bIAheoKIZ6XAXuNJtLQsjw3_8mL_VVV2Tr0y8P6ot3Mnhw6o5LKZMO9g3mPQSI0a-teChl7fiU6GLGVnK0diAAAAAUC8SisA")
BOT_TOKEN = getenv("BOT_TOKEN", "5469255387:AAEwBO6Y3l3qVzZ2_hWv-9bI7w-xiRTqjro")
BOT_NAME = getenv("BOT_NAME", "DADDY")
API_ID = int(getenv("API_ID", "11430350"))
API_HASH = getenv("API_HASH", "eae493b15b16c07b87ed6c84d671d719")
OWNER_NAME = getenv("OWNER_NAME", "DADDY")
OWNER_USERNAME = getenv("OWNER_USERNAME", "PPF88")
ALIVE_NAME = getenv("ALIVE_NAME", "DADDY")
BOT_USERNAME = getenv("BOT_USERNAME", "Dadymusicbot")
OWNER_ID = getenv("OWNER_ID", "1891794672")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "DlIIIlIlD")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "hhhsssoff")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "evvvvs")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5102900434").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/f18958f6e0633b4f38745.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/9e46204fdd365d8a584d1.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/e7167235558834a5c6ae6.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/ab21c3027ff54c410d6a3.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/99940ed14f4420f158643.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
