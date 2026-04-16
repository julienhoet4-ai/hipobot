import os
import requests
from telethon import TelegramClient, events

# Récupération des variables depuis Railway
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")
webhook_url = os.getenv("WEBHOOK_URL")
channel = os.getenv("CHANNEL")

# Connexion du bot
client = TelegramClient("bot", api_id, api_hash).start(bot_token=bot_token)

# Quand un message arrive
@client.on(events.NewMessage(chats=channel))
async def handler(event):
    message = event.message.message

    if message:
        print("Message reçu :", message)

        requests.post(webhook_url, json={
            "content": message
        })

print("✅ Bot lancé et connecté")
client.run_until_disconnected()
