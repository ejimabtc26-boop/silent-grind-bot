import requests
import random
import os
import time
from datetime import datetime
import pytz

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_USERNAME = "@buildinquiet"

timezone = pytz.timezone("Africa/Lagos")

def to_small_caps(text):
    normal = "abcdefghijklmnopqrstuvwxyz"
    small = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for char in text.lower():
        if char in normal:
            result += small[normal.index(char)]
        else:
            result += char
    return result


bible_verses = [
    "Philippians 4:13 — I can do all things through Christ who strengthens me.",
    "Psalm 23:1 — The Lord is my shepherd; I shall not want.",
    "Jeremiah 29:11 — For I know the plans I have for you.",
    "Proverbs 3:5 — Trust in the Lord with all your heart.",
    "Isaiah 41:10 — Fear not, for I am with you.",
    "Romans 8:28 — All things work together for good.",
    "Psalm 121:2 — My help comes from the Lord."
]


def get_prayer(time_of_day):
    verse = random.choice(bible_verses)

    if time_of_day == "morning":
        text = f"""
Good morning Lord.
Thank You for waking us up today.
Order our steps and bless our work.

{verse}

Amen.
"""

    elif time_of_day == "afternoon":
        text = f"""
Heavenly Father,
Renew our strength this afternoon.
Give clarity, peace and productivity.

{verse}

Amen.
"""

    else:
        text = f"""
Father Lord,
Thank You for today.
Grant us peaceful rest tonight.

{verse}

Amen.
"""

    return to_small_caps(text.strip())


def get_image():
    topics = [
        "faith,sunrise",
        "bible,light",
        "prayer,sky",
        "motivation,success"
    ]
    topic = random.choice(topics)
    return f"https://source.unsplash.com/800x600/?{topic}&sig={random.randint(1,100000)}"


def send_photo(photo_url, caption):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    payload = {
        "chat_id": CHANNEL_USERNAME,
        "photo": photo_url,
        "caption": caption
    }
    requests.post(url, data=payload)


while True:
    now = datetime.now(timezone)
    current_time = now.strftime("%H:%M")

    if current_time == "08:10":
        send_photo(get_image(), get_prayer("morning"))
        time.sleep(60)

    elif current_time == "13:00":
        send_photo(get_image(), get_prayer("afternoon"))
        time.sleep(60)

    elif current_time == "18:00":
        send_photo(get_image(), get_prayer("evening"))
        time.sleep(60)

    time.sleep(30)
