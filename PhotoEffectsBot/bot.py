from aiogram import Bot, Dispatcher, types, executor
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from PhotoEffectsBot.pillow_effect import make_filter_image
from keyboards import menu_btn, effects_btn
from database import MainDB
from AllStates import UserStates
import os


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


@dp.message_handler(content_types=['photo'], state=UserStates.get_photo)
async def get_user_photo_state(message: types.Message, state: FSMContext):
    file = await bot.get_file(message.photo[-1].file_id)
    file_type = file.file_path.split(".")[-1]
    filename = f"images/{message.from_user.id}.{file_type}"
    await message.photo[-1].download(destination_file=filename)
    effect = await state.get_data()
    img = await make_filter_image(filename, effect['effect'])
    await message.answer_photo(types.InputFile(img))
    await state.finish()
    os.unlink(img)


@dp.message_handler(content_types=['text'])
async def get_selected_effect_handler(message: types.Message, state: FSMContext):
    text = message.text
    effects = db.get_all_effects()
    effects = list(filter(lambda x: x[0] == text, effects))
    if effects:
        effect = db.get_effect(effects[0][0])
        await state.update_data(effect=effect[0])
        await message.answer("Rasim yuboring:")
        await UserStates.get_photo.set()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
