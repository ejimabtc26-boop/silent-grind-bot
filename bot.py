import requests
import time
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_USERNAME = "@buildinquiet"

def get_motivation():
    quotes = [
    "ᴡᴏʀᴋ ɪɴ ꜱɪʟᴇɴᴄᴇ. ʟᴇᴛ ʀᴇꜱᴜʟᴛꜱ ꜱᴘᴇᴀᴋ.",
    "ᴅɪꜱᴄɪᴘʟɪɴᴇ ᴛᴏᴅᴀʏ. ꜰʀᴇᴇᴅᴏᴍ ᴛᴏᴍᴏʀʀᴏᴡ.",
    "ꜱᴍᴀʟʟ ᴘʀᴏɢʀᴇꜱꜱ ɪꜱ ꜱᴛɪʟʟ ᴘʀᴏɢʀᴇꜱꜱ.",
    "ʏᴏᴜ ᴅɪᴅɴ'ᴛ ᴄᴏᴍᴇ ᴛʜɪꜱ ꜰᴀʀ ᴛᴏ Qᴜɪᴛ.",
    "ꜱɪʟᴇɴᴛ ᴍᴏᴠᴇꜱ. ʟᴏᴜᴅ ʀᴇꜱᴜʟᴛꜱ.",
    "ʜᴜꜱᴛʟᴇ ɪɴ ꜱɪʟᴇɴᴄᴇ ᴀɴᴅ ʟᴇᴛ ꜱᴜᴄᴄᴇꜱꜱ ꜱᴘᴇᴀᴋ.",
    "ɴᴏ ɴᴏɪꜱᴇ — ᴊᴜꜱᴛ ᴘʀᴏɢʀᴇꜱꜱ.",
    "ᴅɪꜱᴄɪᴘʟɪɴᴇ • ꜰᴏᴄᴜꜱ • ɢʀᴏᴡᴛʜ."
    ]
    
    import random
    return random.choice(quotes)

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_USERNAME,
        "text": text
    }
    requests.post(url, data=payload)

while True:
    message = get_motivation()
    send_message(message)
    time.sleep(3600)
