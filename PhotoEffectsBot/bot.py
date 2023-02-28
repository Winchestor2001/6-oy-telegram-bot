from aiogram import Bot, Dispatcher, types, executor
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from PhotoEffectsBot.pillow_effect import make_filter_image
from keyboards import menu_btn, effects_btn, cancel_support_btn
from database import MainDB
from AllStates import UserStates
import os


logging.basicConfig(level=logging.INFO)

BOT_TOKEN = '5674925771:AAE-McW8QREcJ90gSsv2ivWPZEPDr2oEbEM'
ADMIN_GROUP_ID = -1001588256758

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


@dp.message_handler(text='📊 Statistika')
async def show_statistika_handler(message: types.Message):
    total_users = db.count_all_users()
    days, hours = db.count_users_date()
    context = f"Bot azolar soni: {total_users}\n\n" \
              f"1 soat ichida qushilgan azolar: {hours}\n" \
              f"3 kun ichida qushilgan azolar: {days}"
    await message.answer(context)


@dp.message_handler(text='👩‍💻 Biz bilan aloqa')
async def support_handler(message: types.Message):
    btn = await cancel_support_btn()
    await message.answer("Xabaringizni yo`llang:", reply_markup=btn)
    await UserStates.support_message.set()


@dp.message_handler(content_types=['text'], state=UserStates.support_message)
async def support_message_state(message: types.Message, state: FSMContext):
    text = message.text
    user_id = message.from_user.id
    if text == '❌ Bekor qilish':
        btn = await menu_btn()
        await message.answer("Bosh menu", reply_markup=btn)
    else:
        context = f"<a href='tg://user?id={user_id}'>{user_id}</a>\n\n" \
                  f"<em>{text}</em>"
        await bot.send_message(chat_id=ADMIN_GROUP_ID, text=context)

        await message.answer("Sizning xabaringiz adminlarga yuborildi.")

    await state.finish()


@dp.message_handler(content_types=['photo'], state=UserStates.get_photo)
async def get_user_photo_state(message: types.Message, state: FSMContext):
    file = await bot.get_file(message.photo[-1].file_id)
    file_type = file.file_path.split(".")[-1]
    filename = f"images/{message.from_user.id}.{file_type}"
    await message.photo[-1].download(destination_file=filename)
    effect = await state.get_data()
    is_filter = False if effect['effect'] == 'L' else True
    img = await make_filter_image(filename, effect['effect'], is_filter)
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
