import logging
import json

from aiogram import Dispatcher, Bot, executor
from aiogram.types import Message

API_TOKEN = '5674925771:AAE-McW8QREcJ90gSsv2ivWPZEPDr2oEbEM'

# logging settings
logging.basicConfig(level=logging.INFO)

# bot nastroyka qilinadi
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help', 'salom'])
async def bot_start(xabar: Message):
    # print(xabar.text)
    # print(xabar.date)
    # print(xabar.from_user.id)
    # print(xabar.from_id)
    await xabar.answer('Assalomu aleykum.')


if __name__ == '__main__':
    executor.start_polling(dp)
