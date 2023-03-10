from email import message
from telethon import TelegramClient, events, utils
from telethon import types as t
# from telethon.tl.types import PeerUser, PeerChat, PeerChannel
# from telethon.tl.functions.messages import GetDialogsRequest
# # from telethon.tl.types import InputPeerEmpty
# from telethon.tl.custom import Button
#test sdsds sfdgertghfdgh
#test sdfsdfsdf
#gjgorpr;gk



from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import logging
from telethon.tl.functions.channels import JoinChannelRequest
bot = Bot(token="5938016396:AAGt7I3yQgxMWMQfj7evWuDBV8B9z-yLW_c")
dp = Dispatcher(bot)


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)



#Roman
api_id = 11723199
api_hash = '44e5197f69f26f0ea8494a4a7bf53411'
client = TelegramClient('anon', api_id, api_hash)
client.parse_mode = 'html'
client.start()

async def my_groups():

    groups = []
    dialogs = await client.get_dialogs()

    for i in dialogs:

        if i.is_group or i.is_channel:
            groups.append([i.id, i.title])

    x = ['my_groups',groups]
    print(f"SEND ----->>>>{x}")
    print(f"-----------------------------------------")




@client.on(events.NewMessage)
async def my_event_handler(event):

    link=None
    sender = await event.get_sender()
    chat = await event.get_chat()
    username = None
    first_name = None
    last_name = None
    title = None

    if hasattr(event.message.to_id, 'channel_id'):
        print('сообщение пришло в канал (тип channel_id) -------------------------------')
        #print(event)
        print(event.message)
        await client.download_media(event.message.media,"./photo.jpg") 
        if event.message.media:
            if event.message.message:
                with open('./photo.jpg', "rb") as f:
                    await bot.send_photo(5841914430, f,caption=event.message.message)
            else:
                with open('./photo.jpg', "rb") as f:
                    await bot.send_photo(5841914430, f)
        else:
            await bot.send_message(5841914430,event.message.message)
        return
        real_id, peer_type = utils.resolve_id(event.chat_id)
        link = f"https://t.me/c/{real_id}/{event.id}"

        if event.message.message !='':
            if hasattr(sender, 'username'):
                username = f"{sender.username if sender.username != None else ''}"
            if hasattr(sender, 'first_name'):
                first_name = f"{sender.first_name if sender.first_name != None else ''}"

            if hasattr(sender, 'last_name'):
                last_name = f"{sender.last_name if sender.last_name != None else ''}"

            if hasattr(chat, 'title'):
                title = chat.title

            x = ['message_forward', {'chat_id': event.chat_id, 'title': title, 'msg_text':event.message.message, 'username' : username, 'first_name' :first_name, 'last_name': last_name, 'link' :link}]
            print(x)
    if hasattr(event.message.to_id, 'chat_id'):
        print('сообщение в группу (chat_id) ---------------------------------')
        print(event)
        #     chat = await client.get_input_entity(event.message.to_id)


    if hasattr(event.message.to_id, 'user_id'):
        print('сообщение в личку  ------------------------------')
        print(event)
        return


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await client(JoinChannelRequest("DEBUG_KOBZEV"))

    print("debug")
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)
    client.run_until_disconnected()

