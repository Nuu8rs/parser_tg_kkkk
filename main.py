from email import message
from telethon import TelegramClient, events, utils
from telethon import types as t
from Config import api_hash,api_id,Token_bot
from aiogram import Bot, types
from aiogram.utils import executor
import logging
from telethon.tl.functions.channels import JoinChannelRequest
from loader import bot, dp, client
from handlers import __init__




logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)



if __name__ == '__main__':
 
    client.start()
    executor.start_polling(dp)
    client.run_until_disconnected()

