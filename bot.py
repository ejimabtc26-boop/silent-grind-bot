import requests
import random
import os
import time

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_USERNAME = "@buildinquiet"


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


def get_morning_prayer():
    prayer = """
Good morning Lord.
Thank You for the gift of life.
Thank You for waking us up today.

We do not take this breath for granted.
We do not take this day lightly.

Father, guide our steps today.
Order our movements.
Protect our minds.
Protect our energy.
Protect our purpose.

Remove every distraction.
Remove every negativity.
Remove every hidden trap.

Give us discipline.
Give us focus.
Give us strength.
Give us wisdom.
Give us courage.

Bless the work of our hands.
Bless our ideas.
Bless our efforts.
Bless our hustle.
Bless our dreams.

Let doors open today.
Let favor locate us.
Let opportunities find us.

Silence every enemy.
Cancel every delay.
Destroy every doubt.

We choose growth.
We choose peace.
We choose progress.

Today we move with confidence.
Today we walk in purpose.
Today we win.

Amen.
"""
    return to_small_caps(prayer.strip())


def get_image():
    images = [
        "https://source.unsplash.com/800x600/?rap,artist",
        "https://source.unsplash.com/800x600/?success,black-and-white",
        "https://source.unsplash.com/800x600/?prayer,light",
        "https://source.unsplash.com/800x600/?god,sky",
        "https://source.unsplash.com/800x600/?motivation,dark",
        "https://source.unsplash.com/800x600/?luxury,success",
    ]
    return random.choice(images)


def send_photo(photo_url, caption):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    payload = {
        "chat_id": CHANNEL_USERNAME,
        "photo": photo_url,
        "caption": caption
    }
    requests.post(url, data=payload)


while True:
    prayer = get_morning_prayer()
    image_url = get_image()
    send_photo(image_url, prayer)

    # 24 hours
    time.sleep(86400)
