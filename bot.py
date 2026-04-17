@client.on(events.NewMessage(chats=channel))
async def handler(event):
    message = event.message.message or event.message.caption
    entities = event.message.entities

    content = message if message else ""
    links = []

    # récupérer les liens
    if entities and message:
        for entity in entities:
            if hasattr(entity, 'url'):
                links.append(entity.url)

    # ajouter les liens en dessous
    if links:
        content += "\n\n🔗 " + "\n🔗 ".join(links)

    embed = {
        "description": content,
        "color": 5814783
    }

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
