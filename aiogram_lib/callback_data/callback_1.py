import asyncio
import logging
from aiogram import Dispatcher, Bot, executor, types
from keyboards import start_btn, random_img_btn, plus_mines_btn
from random import choice

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = '5674925771:AAE-McW8QREcJ90gSsv2ivWPZEPDr2oEbEM'

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

images = [
    'https://mobimg.b-cdn.net/v3/fetch/22/228503d229ca9ebe8debba9d2bf27025.jpeg',
    'https://www.fonstola.ru/images/201604/fonstola.ru_227429.jpg',
    'https://sibirds.ru/photos/0706/001/07060028201.jpg',
    'https://static.fjcdn.com/large/pictures/1d/6c/1d6c98_5554950.jpg',
]

counter = 0


async def set_commands(dp: Dispatcher):
    await dp.bot.set_my_commands(
        [
            types.BotCommand(command='start', description="Botni ishga tushurish"),
            types.BotCommand(command='help', description='Yordam olish'),
        ]
    )


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    await message.answer_chat_action('typing')
    await message.answer("Assalomu aleykum", reply_markup=start_btn, reply=True)


# @dp.callback_query_handler(text='like')
# @dp.callback_query_handler()
# async def get_callback(callback: types.CallbackQuery):
#     data = callback.data
#     # await callback.answer("Siz 👍 bosdingiz", show_alert=True)
#
#     if data == 'like':
#         await callback.answer("Siz 👍 bosdingiz", show_alert=True)
#     elif data == 'dislike':
#         await callback.answer("Siz 👎 bosdingiz", show_alert=True)
# print(callback.data)
# print(callback.from_user.id)
# print(callback.message.text)
# await callback.answer("Bosildi", show_alert=True)
# await callback.message.answer("Bosildi")


@dp.message_handler(commands=['random'])
async def random_img_handler(message: types.Message):
    imgs = choice(images)
    await message.answer_photo(photo=imgs, reply_markup=random_img_btn)


@dp.callback_query_handler()
async def random_img_callback(callback: types.CallbackQuery):
    data = callback.data

    if data == 'like':
        await callback.answer("❤️", show_alert=True)

    elif data == 'fast':
        await callback.answer("🦅", show_alert=True)

    elif data == 'next':
        img = choice(images)
        # await callback.message.answer_photo(photo=imgs, reply_markup=random_img_btn)
        try:
            await callback.answer()
            await callback.message.edit_media(media=types.InputMedia(media=img, type='photo'),
                                              reply_markup=random_img_btn)
        except:
            await random_img_callback(callback)


@dp.message_handler(commands=['count'])
async def count_handler(message: types.Message):
    await message.answer("0", reply_markup=plus_mines_btn)


#
#
# @dp.callback_query_handler()
# async def count_callback(callback: types.CallbackQuery):
#     global counter
#     data = callback.data
#     if data == 'plus':
#         counter += 1
#     else:
#         if counter == 0:
#             return await callback.answer("0")
#         counter -= 1
#
#     # await callback.answer()
#     await callback.message.edit_text(str(counter), reply_markup=plus_mines_btn)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=set_commands, skip_updates=True)
