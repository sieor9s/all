import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

if os.path.exists("Internal"):
   load_dotenv("Internal")

aiohttpsession = aiohttp.ClientSession()
que = {}
admins = {}

#------------------------ Important Stuff 🤎 -----------------------

API_ID = int(getenv("API_ID", "28311539"))
API_HASH = getenv("API_HASH", "9a7592276f76490009ffadd3f2b2f8a0")
BOT_TOKEN = getenv("BOT_TOKEN", "6269545214:AAE60ylRZwBEPrkngEK4Kopi3zMq2hHnez0")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
STRING_SESSION = getenv("STRING_SESSION", "AgCqwVKbcndeyXWg5OVJvlkk82dG5zA73Tm5zECCPrs6gk6d6zDa-EoSZfFGgK_ifhEJT85YH-wD0b6QtLU4iNelJYRLKE7UzD82RmTIvbDzxfWuyMvWx4XOBHvLhFq9BGmamLVwm1M1sndWYwBE_8zkCgHL7P9s87RGJ5bge2P9PX6X19mKzKZUy4AZYf1DNp1qnwiARj75tgPjNeOqAqS6VA2yDmxGbEX7GOOuO7btG5DnvehtFt86fXGqCEjtJHsrCid8sf2_V3Soyb1Y0Esv_hDS2pOAtDc7mRQ9r8TcdPNAiAoQb5yXYckLn4QrbKEDtdHMEh_6witYN-oM99sRAAAAAWWMR7cA")
BOT_USERNAME = getenv("BOT_USERNAME", "rdos9bot")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5990068364").split()))
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "5990068364").split())
)  # Input type must be interger
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))

#•••••••••••••••••••••••• Mongodb Url Stuff & Loggroupid •••••••••••
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001985844147", "-1001947060305")) 

MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
#________________________ Updates  & Music bot name________________
NETWORK = getenv("NETWORK", "LLYOO")
GROUP = getenv("GROUP", "LLYOO")
BOT_NAME = getenv("BOT_NAME", "Music")
BANNED_USERS = filters.user()

#************************* Image Stuff  ****************************

IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg") 
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://te.legra.ph/file/5fdd8da2461c05d893189.png")

aiohttpsession = aiohttp.ClientSession()


