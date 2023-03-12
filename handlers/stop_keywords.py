from loader import bot,dp,storage
from aiogram.dispatcher import FSMContext
from aiogram import types
from keyboards.stop_keywords import stop_kbd
from aiogram.dispatcher.filters.state import State, StatesGroup
from utils.tools import add_keyword, del_keyword


class Form1(StatesGroup):
    stop_keyword = State()
    
class Form2(StatesGroup):
    del_stop_keyword = State()


@dp.message_handler(text=["/STOP", "/stop", "⛔️STOP слова⛔️"])
async def process_start_command(message: types.Message):
    try:
        with open("keywords.txt", "r") as f:
            keywords = f.read().split(",")
            if len(keywords) == 0:
                msg = "У вас еще нет стоп слов"
            else:
                msg = "Ваш список стоп слов:\n<code>{}</code>".format('\n'.join(keywords))
    except:
        open("keywords.txt", "x")
        msg = "У вас еще нет стоп слов"
    await message.reply(msg, reply_markup=stop_kbd())
    
@dp.callback_query_handler(lambda c: c.data == 'add_stop_keyword')
async def process_callback_button1(call: types.CallbackQuery):
    await Form1.stop_keyword.set()
    await call.message.answer("Введите слово или несколько слов через запятую")

@dp.message_handler(state=Form1.stop_keyword)
async def process_name(message: types.Message, state: FSMContext):
    await state.finish()
    if "," in message.text:
        for word in message.text.split(","):
            add_keyword(word.lstrip().rstrip())
    else:
        add_keyword(message.text.lstrip().rstrip())
    await message.answer("Успешно добавлено")

@dp.callback_query_handler(lambda c: c.data == 'del_stop_keyword')
async def process_callback_button1(call: types.CallbackQuery):
    await Form2.del_stop_keyword.set()
    await call.message.answer("Введите слово или несколько слов через запятую")

@dp.message_handler(state=Form2.del_stop_keyword)
async def process_name(message: types.Message, state: FSMContext):
    await state.finish()
    if "," in message.text:
        for word in message.text.split(","):
            await message.answer(del_keyword(word.lstrip().rstrip()))
    else:
        
        await message.answer(del_keyword(message.text.lstrip().rstrip()))
