from Config import api_hash,api_id, Token_bot
from telethon import TelegramClient, events
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
#Roman

bot = Bot(token=Token_bot)
dp = Dispatcher(bot)
client = TelegramClient('anon', api_id, api_hash)
client.parse_mode = 'html'