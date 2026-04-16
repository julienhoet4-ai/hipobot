from telethon import TelegramClient, events
import requests
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
webhook_url = os.getenv("WEBHOOK_URL")

channel = "@Hipobuyworld"

client = TelegramClient("session", api_id, api_hash)

@client.on(events.NewMessage(chats=channel))
async def handler(event):
    message = event.message.message
    
    if message:
        print("Message:", message)
        requests.post(webhook_url, json={"content": message})

client.start()
print("Connecté avec ton compte")
client.run_until_disconnected()
print("✅ Bot lancé et connecté")
client.run_until_disconnected()
