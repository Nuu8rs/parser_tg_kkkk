from email import message
from telethon import TelegramClient, events, utils
from telethon import types as t
# from telethon.tl.types import PeerUser, PeerChat, PeerChannel
# from telethon.tl.functions.messages import GetDialogsRequest
# # from telethon.tl.types import InputPeerEmpty
# from telethon.tl.custom import Button
from Config import api_hash,api_id,Token_bot
from aiogram import Bot, types
from aiogram.utils import executor
import logging
from telethon.tl.functions.channels import JoinChannelRequest
from loader import bot, dp, client


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    #await client(JoinChannelRequest("DEBUG_KOBZEV"))

    print("debug")
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    
    client.start()
    executor.start_polling(dp)
    client.run_until_disconnected()

