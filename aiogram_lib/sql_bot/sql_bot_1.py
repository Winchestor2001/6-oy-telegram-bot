from aiogram import Dispatcher, Bot, executor, types
import logging
from database import Database

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "5674925771:AAE-McW8QREcJ90gSsv2ivWPZEPDr2oEbEM"

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
db = Database()

db.create_tables()


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
    await message.answer("Assalomu aleykum")


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=set_commands)
