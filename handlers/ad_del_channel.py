from loader import bot,dp,client
from aiogram import Bot, types
from aiogram.dispatcher import FSMContext
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import json

#Кнопка с текстом "📎Добавить канал" 
@dp.message_handler(text_contains="📎Добавить канал",state="*")
async def send_(msg : types.Message, state: FSMContext):   
   await state.finish()
   await msg.answer("Введите ссылку на группу/канал в который бот должен зайти")
   await state.set_state("msg_channel_join")

#Обработка сообщение чтобы подходил по параметрам
@dp.message_handler(state="msg_channel_join")
async def wots(msg : types.Message, state: FSMContext):     
   if "https://t.me/" in msg.text:
      address_chanel = msg.text.split("/")[-1].replace("+","")
      print(address_chanel)
      result = await join_channel(address_chanel)
      if result:
         await msg.answer(f"Бот успешно подключился - <a href='{msg.text}'>Канал</a>")
      else:
         await msg.answer(f"Произошла ошибка при подключении - <a href='{msg.text}'>Канал</a>")
      await state.finish()
   else:
      await msg.answer("Введите коректнные данные")



#Добавление в каналы
async def join_channel(message_chanel):
   try:
      title = await client(JoinChannelRequest(message_chanel))
      await add_to_json(title)
      return True
   except:
      try:
         title = await client(ImportChatInviteRequest(message_chanel))
         await add_to_json(title)
         return True
      except Exception as E:
         print(E)
         res = await client.get_entity("https://t.me/+"+message_chanel)
         print(res)
         return False



async def add_to_json(title):
   id_channel = "-100" + str(title.chats[0].id)
   title_channel = title.chats[0].title
   #str(id_channel):{"Group_Name":title_channel,"Work":"True"}
   with open('file.json', encoding='utf8') as f: 
      data = json.load(f) 
      data[str(id_channel)]={"Group_Name":title_channel,"Work":"True"}
   with open('file.json', 'w', encoding='utf8') as outfile: 
      json.dump(data, outfile, ensure_ascii=False, indent=2) 
      