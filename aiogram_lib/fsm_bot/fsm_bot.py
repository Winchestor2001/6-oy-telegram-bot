from aiogram import Dispatcher, Bot, executor, types
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from keyboards import gander_options_btn

logging.basicConfig(level=logging.INFO)
BOT_TOKEN = "5674925771:AAE-McW8QREcJ90gSsv2ivWPZEPDr2oEbEM"

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class MyStates(StatesGroup):
    first_name = State()
    gander = State()
    phone_number = State()
    avatar = State()


@dp.message_handler(commands=['start'])
async def bot_start_handler(message: types.Message):
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


@dp.callback_query_handler(text_contains='', state=MyStates.gander)
async def select_gander_state(callback: types.CallbackQuery, state: FSMContext):
    pass


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

