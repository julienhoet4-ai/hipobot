from telethon import TelegramClient, events
import requests

api_id = 32836446
api_hash = "44e62ff75a99db3edc5eb653a80154b6"
webhook_url = "https://discord.com/api/webhooks/1494415373603311777/9KYl6vj4V7l4wGZ8XatbHRy7NC-cEDRVpGoHOF9ROrbwo6ba_s0G3gNbNMajdJX70iBJ"

channel = "@Hipobuyworld"

client = TelegramClient("session", api_id, api_hash)

@client.on(events.NewMessage(chats=channel))
async def handler(event):
    message = event.message.message
    
    if message:
        print("Message reçu :", message)
        requests.post(webhook_url, json={"content": message})

client.start()
print("Bot lancé et connecté...")
client.run_until_disconnected()
