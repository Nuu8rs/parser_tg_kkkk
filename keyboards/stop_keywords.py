from aiogram.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton

def stop_kbd():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="add STOP keyword", 
                    callback_data="add_stop_keyword"
                )
            ],
            [
                InlineKeyboardButton(
                    text="delete STOP keyword", 
                    callback_data="del_stop_keyword"
                )
            ]
        ]
    )
