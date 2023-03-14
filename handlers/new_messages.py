from loader import client,bot
from telethon import TelegramClient, events, utils
from telethon.tl.types import MessageMediaPhoto
from keyboards.url_keyboard import url_kbd,url_kbd_2
from utils.tools import format_message, get_keywords
import json
from Config import UserId

text_buffer = []

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
        if " " in word:
            if word in event.message.text.lower():
                print("stop keyword")
                return
        elif word in event.message.text.lower().split():
            print("stop keyword splitted")
            return
    global text_buffer
    for txt in text_buffer:
        if txt == event.message.text or txt in event.message.text:
            print(f"text buffer\n{txt}\n{event.message.text}")
            return
    text_buffer.append(event.message.text)
    if len(text_buffer) > 10:
        text_buffer = text_buffer[-10::1]

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
                                await bot.send_photo(UserId, f,caption=format_message(title, f"({first_name} {last_name}) {username}", event.message.message), reply_markup=url_kbd_2(real_id, event,data.get(channel_id)["Invite_link"]))
                            else:
                                await bot.send_photo(UserId, f,caption=format_message(title, f"({first_name} {last_name}) {username}", event.message.message), reply_markup=url_kbd(real_id, event))
                        except:
                                await bot.send_photo(UserId, f,caption=format_message(title, f"({first_name} {last_name}) {username}", event.message.message), reply_markup=url_kbd(real_id, event))                            
                else:
                    with open('./photo.jpg', "rb") as f:
                        try:
                            if data.get(channel_id)["Type"] == "Chat":
                                await bot.send_photo(UserId, f, reply_markup=url_kbd_2(real_id, event,data.get(channel_id)["Invite_link"]))
                            else:
                                await bot.send_photo(UserId, f, reply_markup=url_kbd(real_id, event))
                        except:
                                await bot.send_photo(UserId, f, reply_markup=url_kbd(real_id, event))                            
            else:
                if event.message.message:
                    try:
                        if data.get(channel_id)["Type"] == "Chat":
                            await bot.send_message(UserId,format_message(title, f"({first_name} {last_name}) {username}", event.message.message), reply_markup=url_kbd_2(real_id, event,data.get(channel_id)["Invite_link"]))
                        else:
                            await bot.send_message(UserId,format_message(title, f"({first_name} {last_name}) {username}", event.message.message), reply_markup=url_kbd(real_id, event))
                    except:
                        await bot.send_message(UserId,format_message(title, f"({first_name} {last_name}) {username}", event.message.message), reply_markup=url_kbd(real_id, event))
        return

