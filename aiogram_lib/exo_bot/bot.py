import logging
import json

from aiogram import Dispatcher, Bot, executor
from aiogram.types import Message, InputFile

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
    # await bot.send_message(chat_id=1097652234, text='Xayr')


@dp.message_handler(content_types=['text', 'voice'])
async def text_handler(xabar: Message):
    tip = xabar.content_type
    if tip == 'text':
        pic = InputFile('pic.png')
        await xabar.answer_photo(photo=pic, caption="Bu rasim!")
    else:
        await bot.send_voice(chat_id=5135652528, voice=xabar.voice.file_id, caption="Bu audio")
    # print(xabar)
    # await xabar.answer_voice(voice=xabar.voice.file_id)
    # await bot.send_voice(chat_id=5135652528, voice=xabar.voice.file_id)


if __name__ == '__main__':
    executor.start_polling(dp)
