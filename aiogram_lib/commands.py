import asyncio
import logging
from aiogram import Dispatcher, Bot, executor, types
from random import choice

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = '5674925771:AAE-McW8QREcJ90gSsv2ivWPZEPDr2oEbEM'

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
count = 1


async def set_commands(dp: Dispatcher):
    await dp.bot.set_my_commands(
        [
            types.BotCommand(command='start', description="Botni ishga tushurish"),
            types.BotCommand(command='help', description='Yordam olish'),
        ]
    )


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    await message.answer("Salom")


@dp.message_handler(commands=['help'])
async def help_bot(message: types.Message):
    context = f"""
            Bot commands:\n\n
    /start = Botni ishga tushurish\n
    /count = Commandani ishlatilgan soni\n
    /sticker = Sticker jo'natish\n
    /emoji = Emoji jo'natish\n
    /uzb = Uzb bayrog'i
            """
    await message.answer(context)


@dp.message_handler(commands=['count'])
async def counter_handler(message: types.Message):
    global count
    await message.answer(f"Click: {count}")
    count += 1


@dp.message_handler(commands=['sticker'])
async def sticker_handler(message: types.Message):
    await message.reply_sticker('CAACAgIAAxkBAAEHc9Nj0kthyNZl4VnXEUdtMt9MPgIw6wACbhIAArzW1AShMO-Heha9QS0E')
    await message.reply_sticker('CAACAgIAAxkBAAEHc9Vj0ktpZ661Pwp-qBFZnbag3YmAsAACNBMAAjGSoEvT_Q2YdUoyGS0E')


@dp.message_handler(content_types=['text'])
async def emoji_handler(message: types.Message):
    if message.text == 'emoji':
        emojies = ['😇', '🥸', '🤯', '🥶', '🤑']
        await message.answer(f"Siz {choice(emojies)}")
        # await message.delete()
        await asyncio.sleep(5)
        await bot.delete_message(message.chat.id, message.message_id + 1)
    else:
        await message.reply("Sizni tushunmadim!")


@dp.message_handler(commands=['uzb'])
async def uzbekcha_handler(message: types.Message):
    context = f'Uzbekistan\n' \
              f'<b>Uzbekistan</b>\n' \
              f'<em>Uzbekistan</em>\n' \
              f'<u>Uzbekistan</u>\n' \
              f'<s>Uzbekistan</s>\n' \
              f'<tg-spoiler>Uzbekistan</tg-spoiler>\n' \
              f'<a href="https://youtu.be/vQVwkyn3-F8">Uzbekistan</a>\n' \
              f'<code>Uzbekistan</code>\n' \
              f'<pre>Uzbekistan</pre>'
    await message.answer_photo(photo='https://www.advantour.com/img/uzbekistan/symbolics/uzbekistan-flag.jpg',
                               caption=context)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=set_commands, skip_updates=True)
