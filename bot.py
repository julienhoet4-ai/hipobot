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
    try:
        # récupérer texte OU caption
        message = event.message.message or event.message.caption
        entities = event.message.entities

        content = message if message else ""
        links = []

        # récupérer les liens
        if entities and message:
            for entity in entities:
                if hasattr(entity, 'url'):
                    links.append(entity.url)

        # ajouter liens en dessous
        if links:
            content += "\n\n🔗 " + "\n🔗 ".join(links)

        embed = {
            "description": content,
            "color": 5814783
        }

        # si image
        if event.message.photo:
            file_path = await event.message.download_media()

            if file_path and os.path.exists(file_path):
                embed["image"] = {"url": "attachment://image.jpg"}

                with open(file_path, "rb") as f:
                    requests.post(
                        webhook_url,
                        data={"payload_json": json.dumps({"embeds": [embed]})},
                        files={"file": ("image.jpg", f)}
                    )
            else:
                # fallback si image bug
                requests.post(
                    webhook_url,
                    json={"embeds": [embed]}
                )
        else:
            requests.post(
                webhook_url,
                json={"embeds": [embed]}
            )

    except Exception as e:
        print("ERREUR :", e)

client.start()
print("Bot connecté")
client.run_until_disconnected()
