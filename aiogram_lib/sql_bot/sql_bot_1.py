from aiogram import Dispatcher, Bot, executor, types
import logging
from database import Database

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "5674925771:AAE-McW8QREcJ90gSsv2ivWPZEPDr2oEbEM"

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
db = Database()

db.create_tables()

menu_btn = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu_btn.add(
    types.KeyboardButton("Tilni o'zgartirish")
)

langs_btn = types.InlineKeyboardMarkup(row_width=2)
langs_btn.add(
    types.InlineKeyboardButton("🇷🇺", callback_data="ru"),
    types.InlineKeyboardButton("🇺🇿", callback_data="uz")
)

messages = {
    'uz': {'start_text': 'Assalomu aleykum', 'select_lang': 'Tilni tanlang'},
    'ru': {'start_text': 'Привет, как ты', 'select_lang': 'Выберите язык'},
}


async def set_commands(dp: Dispatcher):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Assalomu aleykum"),
        ]
    )


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username
    db.add_user(user_id=user_id, username=username)

    user_lang = db.get_user_info(user_id)

    await message.answer(messages[user_lang[2]]['start_text'], reply_markup=menu_btn)


@dp.message_handler(commands=['users'])
async def show_all_users_handler(message: types.Message):
    users = db.get_all_users()
    context = f'Userlar soni: {len(users)}\n\n' \
              f'Userlar:\n'

    for n, user in enumerate(users, start=1):
        context += f"{n}) {user[1]}\n"

    await message.answer(context)


@dp.message_handler(text="Tilni o'zgartirish")
async def change_lang_handler(message: types.Message):
    user_lang = db.get_user_info(message.from_user.id)
    await message.answer(messages[user_lang[2]]['select_lang'], reply_markup=langs_btn)


@dp.callback_query_handler(text='uz')
async def selected_uz_callback(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    db.update_user_lang(user_id=user_id, lang='uz')
    await callback.answer("Til o'zgardi", show_alert=True)


@dp.callback_query_handler(text='ru')
async def selected_ru_callback(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    db.update_user_lang(user_id=user_id, lang='ru')
    await callback.answer("Til o'zgardi", show_alert=True)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=set_commands)
