import requests
import random
import os
import time

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_USERNAME = "@buildinquiet"

def to_small_caps(text):
    normal = "abcdefghijklmnopqrstuvwxyz"
    small  = "ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘǫʀꜱᴛᴜᴠᴡxʏᴢ"
    result = ""
    for char in text.lower():
        if char in normal:
            result += small[normal.index(char)]
        else:
            result += char
    return result

def get_motivation():
    quotes = [
        "work in silence. let results speak.",
        "discipline today. freedom tomorrow.",
        "small progress is still progress.",
        "you didn’t come this far to quit.",
        "silent moves. loud results.",
        "hustle in silence and let success speak.",
        "no noise — just progress.",
        "discipline • focus • growth."
    ]
    return to_small_caps(random.choice(quotes))

def send_photo(photo_url, caption):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    payload = {
        "chat_id": CHANNEL_USERNAME,
        "photo": photo_url,
        "caption": caption
    }
    requests.post(url, data=payload)

while True:
    quote = get_motivation()
    image_url = "https://picsum.photos/800/600"

    send_photo(image_url, quote)

    time.sleep(3600)
