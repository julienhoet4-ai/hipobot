@client.on(events.NewMessage(chats=channel))
async def handler(event):
    message = event.message.message
    entities = event.message.entities

    content = message if message else ""

    # Transformer liens cachés en markdown cliquable
    if entities and message:
        for entity in entities:
            if hasattr(entity, 'url'):
                text = message[entity.offset:entity.offset + entity.length]
                url = entity.url
                content = content.replace(text, f"[{text}]({url})")

    embed = {
        "description": content,
        "color": 5814783  # couleur bleu stylé
    }

    # IMAGE dans le même bloc
    if event.message.photo:
        file = await event.message.download_media()
        embed["image"] = {"url": "attachment://image.jpg"}

        with open(file, "rb") as f:
            requests.post(
                webhook_url,
                data={"payload_json": str({"embeds": [embed]})},
                files={"file": ("image.jpg", f)}
            )
    else:
        requests.post(
            webhook_url,
            json={"embeds": [embed]}
        )
