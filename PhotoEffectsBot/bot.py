from aiogram import Bot, Dispatcher, types, executor
import logging

from aiogram.contrib.fsm_storage.memory import MemoryStorage

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = '5674925771:AAE-McW8QREcJ90gSsv2ivWPZEPDr2oEbEM'

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def bot_start_handler(message: types.Message):
    await message.answer("Assalomu aleykum")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
