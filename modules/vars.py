import os

API_ID    = os.environ.get("API_ID", "20246426")
API_HASH  = os.environ.get("API_HASH", "77330c674fb1056fa7029a657075d2dc")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8000))  # Default to 8000 if not set
