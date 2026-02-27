import requests
import time
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_USERNAME = "@buildinquiet"

def get_motivation():
    quotes = [
        "Stay grinding. Success is coming.",
        "Discipline today. Freedom tomorrow.",
        "Small progress is still progress.",
        "You didn't come this far to quit.",
        "Silent moves. Loud results.",
        "Hustle in silence and let success speak."
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
