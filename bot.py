from telethon import TelegramClient, events
from telethon.sessions import StringSession
import requests
import os
import json

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

    content = message if message else ""

    # 🔗 Transformer liens cachés en liens cliquables
    if entities and message:
        for entity in entities:
            if hasattr(entity, 'url'):
                text = message[entity.offset:entity.offset + entity.length]
                url = entity.url
                content = content.replace(text, f"[{text}]({url})")

    # 💎 Création embed Discord
    embed = {
        "description": content,
        "color": 5814783
    }

    # 📸 Si image
    if event.message.photo:
        file = await event.message.download_media()
        embed["image"] = {"url": "attachment://image.jpg"}

        with open(file, "rb") as f:
            requests.post(
                webhook_url,
                data={
                    "payload_json": json.dumps({"embeds": [embed]})
                },
                files={
                    "file": ("image.jpg", f)
                }
            )
    else:
        requests.post(
            webhook_url,
            json={"embeds": [embed]}
        )

client.start()
print("Bot connecté")
client.run_until_disconnected()
