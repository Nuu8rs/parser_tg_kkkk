from aiogram.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from loader import client
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import json

def url_kbd(real_id, event):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🔗", 
                    url=f"https://t.me/c/{real_id}/{event.id}"
                )
            ]
        ]
    )


