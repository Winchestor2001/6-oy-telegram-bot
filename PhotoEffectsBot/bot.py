from aiogram import Bot, Dispatcher, types
import logging

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = ''

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

