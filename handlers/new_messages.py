from loader import client,bot
from telethon import TelegramClient, events, utils

@client.on(events.NewMessage)
async def my_event_handler(event):

    link=None
    sender = await event.get_sender()
    chat = await event.get_chat()
    username = None
    first_name = None
    last_name = None
    title = None

    if hasattr(event.message.to_id, 'channel_id'):
        print(event.message)
        await client.download_media(event.message.media,"./photo.jpg") 
        if event.message.media:
            if event.message.message:
                with open('./photo.jpg', "rb") as f:
                    await bot.send_photo(5841914430, f,caption=event.message.message)
            else:
                with open('./photo.jpg', "rb") as f:
                    await bot.send_photo(5841914430, f)
        else:
            await bot.send_message(5841914430,event.message.message)
        return
        real_id, peer_type = utils.resolve_id(event.chat_id)
        link = f"https://t.me/c/{real_id}/{event.id}"

        if event.message.message !='':
            if hasattr(sender, 'username'):
                username = f"{sender.username if sender.username != None else ''}"
            if hasattr(sender, 'first_name'):
                first_name = f"{sender.first_name if sender.first_name != None else ''}"

            if hasattr(sender, 'last_name'):
                last_name = f"{sender.last_name if sender.last_name != None else ''}"

            if hasattr(chat, 'title'):
                title = chat.title

            x = ['message_forward', {'chat_id': event.chat_id, 'title': title, 'msg_text':event.message.message, 'username' : username, 'first_name' :first_name, 'last_name': last_name, 'link' :link}]
            print(x)
    if hasattr(event.message.to_id, 'chat_id'):
        print(event)
        #     chat = await client.get_input_entity(event.message.to_id)


        print(event)
        return

