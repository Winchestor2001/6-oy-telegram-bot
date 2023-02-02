import asyncio
from random import randint
import logging
from aiogram import Dispatcher, Bot, executor, types

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = '5674925771:AAE-McW8QREcJ90gSsv2ivWPZEPDr2oEbEM'

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

start_menu_btn = types.ReplyKeyboardMarkup(resize_keyboard=True)
start_menu_btn.row("Biz Xaqimizda", "Contact")

about_btn = types.ReplyKeyboardMarkup(resize_keyboard=True)
about_btn.row("Video konsultatsiya")
about_btn.row("Ortga")

contact_btn = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
contact_btn.add(
    types.KeyboardButton("Location"),
    types.KeyboardButton("Telefon raqamlar"),
    types.KeyboardButton("Ortga"),
)


async def set_commands(dp: Dispatcher):
    await dp.bot.set_my_commands(
        [
            types.BotCommand(command='start', description="Botni ishga tushurish"),
            types.BotCommand(command='help', description='Yordam olish'),
        ]
    )


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    await message.answer("Assalomu aleykum", reply_markup=start_menu_btn)


@dp.message_handler(content_types=['text'])
async def any_btn_handler(message: types.Message):
    text = message.text

    if text == 'Biz Xaqimizda':
        await message.answer("Biz Nits Python guruximiz!", reply_markup=about_btn)

    elif text == 'Contact':
        name = message.from_user.first_name
        t = f"<b>{name}</b>"
        await message.answer("Biz bilan zudlikbilan bog'laning!", reply_markup=contact_btn)

    elif text == 'Ortga':
        # await start_bot(message)
        await message.answer("Assalomu aleykum", reply_markup=start_menu_btn)

    elif text == 'Video konsultatsiya':
        video = types.InputFile('video/video.mp4')
        await message.answer_video(video, width=400, height=60)

    elif text == 'Location':
        lat = randint(10, 100)
        lon = randint(30, 60)
        await message.answer_location(latitude=lat, longitude=lon)

    elif text == 'Telefon raqamlar':
        await message.answer_contact(phone_number='+998913451175', first_name="Bexruz")
        await message.answer_contact(phone_number='+998995354994', first_name="Odiljon")
        await message.answer_contact(phone_number='+998931333839', first_name="Ozodbek")


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=set_commands, skip_updates=True)
