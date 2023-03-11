from aiogram.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton

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