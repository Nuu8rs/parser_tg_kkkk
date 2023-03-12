from aiogram.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from loader import client
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import json


async def get_all_channel_keyboard():
    menu_channel_buutons = InlineKeyboardMarkup(row_width=2)
    emodj = {"True":"✅","False":"❌"}
    f = open("file.json","r",encoding="UTF-8")
    data = json.load(f)
    for key,channel in data.items():
        text_msg = emodj[channel.get("Work")] + " " + channel.get("Group_Name")
        button = InlineKeyboardButton(text=text_msg,callback_data=f"channel:{key}")
        menu_channel_buutons.insert(button)
    butt = InlineKeyboardButton(text="➕ Добавить канал",callback_data="channel_add")
    menu_channel_buutons.add(butt)
    return menu_channel_buutons
        

async def change_keyboard_channel(id_channel):
    f = open("file.json","r+",encoding="UTF-8")
    data = json.load(f)

    
    status_work =  str(False if data.get(id_channel)["Work"] == "True" else True)
    data.get(id_channel)["Work"] = status_work
    with open('file.json', 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=2)
    menu_channel_buutons = InlineKeyboardMarkup(row_width=2)
    emodj = {"True":"✅","False":"❌"}

    for key,channel in data.items():
        text_msg = emodj[channel.get("Work")] + " " + channel.get("Group_Name")
        button = InlineKeyboardButton(text=text_msg,callback_data=f"channel:{key}")
        menu_channel_buutons.insert(button)
    butt = InlineKeyboardButton(text="➕ Добавить канал",callback_data="channel_add")
    menu_channel_buutons.add(butt)
    return menu_channel_buutons 