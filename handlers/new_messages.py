from loader import client,bot
from telethon import TelegramClient, events, utils
from telethon.tl.types import MessageMediaPhoto
from keyboards.url_keyboard import url_kbd,url_kbd_2
from utils.tools import format_message, get_keywords
import json
@client.on(events.NewMessage)
async def my_event_handler(event):

    link=None
    sender = await event.get_sender()
    chat = await event.get_chat()
    username = None
    first_name = None
    last_name = None
    title = None


    real_id, peer_type = utils.resolve_id(event.chat_id)
    if hasattr(sender, 'username') and not sender.username is None:
        username = '@'+sender.username
    else:
        username = ''
    if hasattr(sender, 'first_name') and not sender.first_name is None:
        first_name = sender.first_name
    else:
        first_name = ''
    if hasattr(sender, 'last_name') and not sender.last_name is None:
        last_name = sender.last_name
    else:
        last_name = ''
    if hasattr(chat, 'title'):
        title = chat.title
    for word in get_keywords():
        if word in event.message.text.split():
            return
    try:
        channel_id = "-100"+str(event.message.peer_id.channel_id)
    except:
        channel_id = "-100"+str(event.message.to_id.chat_id)
    f = open("file.json","r+",encoding="UTF-8")
    data = json.load(f)
    if channel_id in data:
        if data.get(channel_id)["Work"] == "True":
            
            if isinstance(event.message.media, MessageMediaPhoto):
                await client.download_media(event.message.media,"./photo.jpg") 
                if event.message.message:
                    with open('./photo.jpg', "rb") as f:
                        try:
                            if data.get(channel_id)["Type"] == "Chat":
                                await bot.send_photo(5456085368, f,caption=format_message(title, f"({first_name} {last_name}) {username}", event.message.message), reply_markup=url_kbd_2(real_id, event,data.get(channel_id)["Invite_link"]))
                            else:
                                await bot.send_photo(5456085368, f,caption=format_message(title, f"({first_name} {last_name}) {username}", event.message.message), reply_markup=url_kbd(real_id, event))
                        except:
                                await bot.send_photo(5456085368, f,caption=format_message(title, f"({first_name} {last_name}) {username}", event.message.message), reply_markup=url_kbd(real_id, event))                            
                else:
                    with open('./photo.jpg', "rb") as f:
                        try:
                            if data.get(channel_id)["Type"] == "Chat":
                                await bot.send_photo(5456085368, f, reply_markup=url_kbd_2(real_id, event,data.get(channel_id)["Invite_link"]))
                            else:
                                await bot.send_photo(5456085368, f, reply_markup=url_kbd(real_id, event))
                        except:
                                await bot.send_photo(5456085368, f, reply_markup=url_kbd(real_id, event))                            
            else:
                if event.message.message:
                    try:
                        if data.get(channel_id)["Type"] == "Chat":
                            await bot.send_message(5456085368,format_message(title, f"({first_name} {last_name}) {username}", event.message.message), reply_markup=url_kbd_2(real_id, event,data.get(channel_id)["Invite_link"]))
                        else:
                            await bot.send_message(5456085368,format_message(title, f"({first_name} {last_name}) {username}", event.message.message), reply_markup=url_kbd(real_id, event))
                    except:
                        await bot.send_message(5456085368,format_message(title, f"({first_name} {last_name}) {username}", event.message.message), reply_markup=url_kbd(real_id, event))
        return

