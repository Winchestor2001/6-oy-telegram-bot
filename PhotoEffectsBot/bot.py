from aiogram import Bot, Dispatcher, types, executor
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from keyboards import menu_btn, effects_btn
from database import MainDB


logging.basicConfig(level=logging.INFO)

BOT_TOKEN = '5674925771:AAE-McW8QREcJ90gSsv2ivWPZEPDr2oEbEM'

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = MainDB()
db.create_tables()


@dp.message_handler(commands=['start'])
async def bot_start_handler(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username
    db.add_user(user_id, username)

    btn = await menu_btn()
    await message.answer("Assalomu aleykum", reply_markup=btn)


@dp.message_handler(text='🔙 Ortga')
async def back_btn_handler(message: types.Message):
    btn = await menu_btn()
    await message.answer("Bosh menu", reply_markup=btn)


@dp.message_handler(content_types=['text'], text='🖼 Rasimga Joziba berish')
async def show_effects_handler(message: types.Message):
    effects = db.get_all_effects()
    btn = await effects_btn(effects)
    await message.answer("Effectni tanlang:", reply_markup=btn)


@dp.message_handler(content_types=['text'])
async def get_selected_effect_handler(message: types.Message, state: FSMContext):
    text = message.text
    effects = db.get_all_effects()
    effects = list(filter(lambda x: x[0] == text, effects))
    if effects:
        effect = db.get_effect(effects[0][0])
        await state.update_data(effect=effect[0])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
