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
    
    if message:
        print("Message:", message)
        requests.post(webhook_url, json={"content": message})

client.start()
print("Bot connecté")
client.run_until_disconnected()
