@client.on(events.NewMessage(chats=channel))
async def handler(event):
    message = event.message.message
    entities = event.message.entities

    content = ""

    if message:
        content = message

        # Transformer les liens cachés en liens cliquables
        if entities:
            for entity in entities:
                if hasattr(entity, 'url'):
                    text = message[entity.offset:entity.offset + entity.length]
                    url = entity.url
                    markdown_link = f"[{text}]({url})"
                    content = content.replace(text, markdown_link)

        print("Message:", content)
        requests.post(webhook_url, json={"content": content})

    # IMAGE
    if event.message.photo:
        file = await event.message.download_media()
        with open(file, "rb") as f:
            requests.post(webhook_url, files={"file": f})
