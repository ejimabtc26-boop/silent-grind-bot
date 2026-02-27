import requests
import random
import os
import time
from datetime import datetime
import pytz

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_USERNAME = "@buildinquiet"

# Nigeria Timezone
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


# Bible verses (rotates daily)
bible_verses = [
    "Philippians 4:13 — I can do all things through Christ who strengthens me.",
    "Psalm 23:1 — The Lord is my shepherd; I shall not want.",
    "Jeremiah 29:11 — For I know the plans I have for you.",
    "Proverbs 3:5 — Trust in the Lord with all your heart.",
    "Isaiah 41:10 — Fear not, for I am with you.",
    "Romans 8:28 — All things work together for good.",
    "Psalm 121:2 — My help comes from the Lord.",
]


def get_prayer(time_of_day):
    verse = random.choice(bible_verses)

    if time_of_day == "morning":
        prayer = f"""
Good morning Lord.
Thank You for the gift of life.
Thank You for waking us up today.

As we step into this new day,
Order our steps.
Protect our minds.
Protect our peace.
Protect our purpose.

Give us strength to win.
Give us focus to stay disciplined.
Give us courage to face challenges.

Let favor locate us.
Let doors open.
Let opportunities find us.

Bless the work of our hands.
Bless our hustle.
Bless our dreams.

Destroy every delay.
Silence every enemy.
Cancel every doubt.

Today we move with confidence.
Today we grow.
Today we win.

{verse}

Amen.
"""

    elif time_of_day == "afternoon":
        prayer = f"""
Heavenly Father,

As we continue this day,
Renew our strength.

Where we feel tired,
Refresh us.

Where we feel confused,
Give clarity.

Where we feel pressure,
Give peace.

Bless our efforts this afternoon.
Let productivity increase.
Let wisdom guide decisions.

Shield us from mistakes.
Shield us from negativity.
Shield us from hidden traps.

Let our name be mentioned for favor.
Let grace speak for us.

{verse}

We remain grateful.
Amen.
"""

    else:  # evening
        prayer = f"""
Father Lord,

As the day comes to an end,
We say thank You.

Thank You for protection.
Thank You for provision.
Thank You for guidance.

Forgive our mistakes.
Cleanse our hearts.
Renew our spirit.

As we rest tonight,
Grant peaceful sleep.

Protect our homes.
Protect our families.
Protect our future.

Prepare tomorrow’s success.
Prepare new blessings.
Prepare new opportunities.

{verse}

We trust You.
Amen.
"""

    return to_small_caps(prayer.strip())


def get_image():
    topics = [
        "faith,light",
        "bible,sunrise",
        "prayer,sky",
        "motivation,black-and-white",
        "greatness,leader",
        "success,focus",
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


last_posted = None

while True:
    now = datetime.now(timezone)
    current_hour = now.hour

    if current_hour == 8 and last_posted != "morning":
        send_photo(get_image(), get_prayer("morning"))
        last_posted = "morning"

    elif current_hour == 13 and last_posted != "afternoon":
        send_photo(get_image(), get_prayer("afternoon"))
        last_posted = "afternoon"

    elif current_hour == 18 and last_posted != "evening":
        send_photo(get_image(), get_prayer("evening"))
        last_posted = "evening"

    time.sleep(60)
