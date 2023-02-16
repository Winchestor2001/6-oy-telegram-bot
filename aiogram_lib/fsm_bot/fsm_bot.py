from aiogram import Dispatcher, Bot, executor, types
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from keyboards import gander_options_btn, send_phone_number_btn, remove_btn
from database import MainDB

logging.basicConfig(level=logging.INFO)
BOT_TOKEN = "5674925771:AAE-McW8QREcJ90gSsv2ivWPZEPDr2oEbEM"

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = MainDB()
db.create_tables()


class MyStates(StatesGroup):
    first_name = State()
    gander = State()
    phone_number = State()
    avatar = State()


@dp.message_handler(commands=['start'])
async def bot_start_handler(message: types.Message):
    db.save_user(message.from_user.id)
    await message.answer('Salom')


@dp.message_handler(commands=['reg'])
async def bot_reg_handler(message: types.Message):
    await message.answer('Ism kiriting:')
    await MyStates.first_name.set()


@dp.message_handler(state=MyStates.first_name)
async def bot_first_name_state(message: types.Message, state: FSMContext):
    text = message.text

    await state.update_data(ism=text)
    btn = await gander_options_btn()
    await message.answer("Jinsingizni tanlang:", reply_markup=btn)
    await MyStates.gander.set()


@dp.callback_query_handler(text_contains='gander:', state=MyStates.gander)
async def select_gander_state(callback: types.CallbackQuery, state: FSMContext):
    gander = callback.data.split(":")[-1]
    await state.update_data(gander=gander)
    btn = await send_phone_number_btn()
    await callback.message.answer("Telefon raqamni yuboring", reply_markup=btn)
    await MyStates.phone_number.set()


@dp.message_handler(content_types=['contact'], state=MyStates.phone_number)
async def get_phone_number_state(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.contact.phone_number)
    await message.answer("Rasimingizni yuboring:", reply_markup=remove_btn)
    await MyStates.avatar.set()


@dp.message_handler(content_types=['photo'], state=MyStates.avatar)
async def get_avatar_state(message: types.Message, state: FSMContext):
    pic_id = message.photo[-1].file_id
    data = await state.get_data()
    db.save_user_data(
        user_id=message.from_user.id,
        data=data,
        img=pic_id
    )
    await message.answer("Siz ro`yxatdan o`tingiz!")
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
