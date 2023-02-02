import asyncio
import logging
from aiogram import Dispatcher, Bot, executor, types

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = '5674925771:AAE-McW8QREcJ90gSsv2ivWPZEPDr2oEbEM'

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


async def set_commands(dp: Dispatcher):
    await dp.bot.set_my_commands(
        [
            types.BotCommand(command='start', description="Botni ishga tushurish"),
            types.BotCommand(command='help', description='Yordam olish'),
        ]
    )


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    await message.answer("Assalomu aleykum")


@dp.message_handler(commands=['media'])
async def send_medies_handler(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('img/6. Жираф.jpg'))
    media.attach_photo(types.InputFile('img/10. Цветы.jpg'))
    media.attach_video(types.InputFile('video/video.mp4'))
    await message.answer_chat_action('upload_photo')
    # actions: upload_photo, upload_video, upload_audio, record_voice, typing, record_video,
    # upload_voice, upload_document, find_location, choose_sticker
    # media.attach_photo(types.InputFile('img/16. Город.jpg'))
    # media.attach_photo(types.InputFile('img/9. Пустыня.jpg'))

    await message.answer_media_group(media=media)
    # await bot.send_media_group(message.from_user.id, media=media)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=set_commands, skip_updates=True)