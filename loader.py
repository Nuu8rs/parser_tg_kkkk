from Config import api_hash,api_id, Token_bot
from telethon import TelegramClient, events
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
#Roman

bot = Bot(token=Token_bot,parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()   
dp = Dispatcher(bot,storage=storage)

client = TelegramClient('anon', api_id, api_hash)
client.parse_mode = 'html'