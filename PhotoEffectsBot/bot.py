from aiogram import Bot, Dispatcher, types, executor
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboards import menu_btn
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


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
