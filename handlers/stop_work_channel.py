from loader import bot,dp,client
from aiogram import Bot, types
from aiogram.dispatcher import FSMContext
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import LeaveChannelRequest
from keyboards.keyboard_bot import get_all_channel_keyboard , change_keyboard_channel


@dp.message_handler(text=["Ваши чаты","/start"],state="*")
async def send_(msg : types.Message, state: FSMContext):   
    await state.finish()
    await msg.answer("<b>Ваши каналы</b>",reply_markup= await get_all_channel_keyboard())


@dp.callback_query_handler(text_contains="channel")
async def callb(call: types.CallbackQuery,state:FSMContext):
    id_channel = call.data.split(":")[-1]
    await call.message.edit_reply_markup(reply_markup=await change_keyboard_channel(id_channel))