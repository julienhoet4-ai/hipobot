from telethon import TelegramClient, events
from telethon.sessions import StringSession
import requests
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session = os.getenv("SESSION")
webhook_url = os.getenv("WEBHOOK_URL")

channel = "@Hipobuyworld"

client = TelegramClient(StringSession(session), api_id, api_hash)

@client.on(events.NewMessage(chats=channel))
async def handler(event):
    message = event.message.message
    entities = event.message.entities

    content = ""

    # TEXTE + LIENS CACHÉS
    if message:
        content = message

        if entities:
            for entity in entities:
                if hasattr(entity, 'url'):
                    content += f"\n🔗 {entity.url}"

        print("Message:", content)
        requests.post(webhook_url, json={"content": content})

    # IMAGE
    if event.message.photo:
        file = await event.message.download_media()
        with open(file, "rb") as f:
            requests.post(webhook_url, files={"file": f})

client.start()
print("Bot connecté")
client.run_until_disconnected()
print("Bot connecté")
client.run_until_disconnected()
