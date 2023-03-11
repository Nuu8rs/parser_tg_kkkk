from loader import bot,dp,client
from aiogram import Bot, types
from aiogram.dispatcher import FSMContext
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import LeaveChannelRequest

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
      address_chanel = msg.text.split("/")[-1]
      print(address_chanel)
      result = await join_channel(address_chanel)
      if result:
         await msg.answer(f"Бот успешно подключился - <a href='{msg.text}'>Канал</a>")
      else:
         await msg.answer(f"Произошла ошибка при подключении - <a href='{msg.text}'>Канал</a>")
      await state.finish()
   else:
      await msg.answer("Введите коректнные данные")

#Кнопка с текстом "📎Выйти с канала" 
@dp.message_handler(text_contains="📎Выйти с канала",state="*")
async def send_(msg : types.Message, state: FSMContext):   
   await state.finish()
   await msg.answer("Введите ссылку на группу/канал с которого бот должен выйти")
   await state.set_state("msg_channel_leave")

#Обработка сообщение чтобы подходил по параметрам
@dp.message_handler(state="msg_channel_leave")
async def wots(msg : types.Message, state: FSMContext):     
   if "https://t.me/" in msg.text:
      address_chanel = msg.text.split("/")[-1]
      print(address_chanel)
      result = await leave_channel(address_chanel)
      if result:
         await msg.answer(f"Бот успешно вышел с чата - <a href='{msg.text}'>Канал</a>")
      else:
         await msg.answer(f"Произошла ошибка при выходе с чата - <a href='{msg.text}'>Канал</a>")
      await state.finish()
   else:
      await msg.answer("Введите коректнные данные")

#Добавление в каналы
async def join_channel(message_chanel):
   try:
      await client(JoinChannelRequest(message_chanel))
      return True
   except:
      try:
         await client(ImportChatInviteRequest(message_chanel))
         return True
      except Exception as E:
         print(E)
         return False
#Выход с каналов
async def leave_channel(message_chanel):
   try:
      await client(LeaveChannelRequest(message_chanel))
      return True
   except Exception as E:
      return False   