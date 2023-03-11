from loader import bot,dp
from aiogram import Bot, types

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    print("debug")
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


