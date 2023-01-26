import logging
from aiogram import Dispatcher, Bot, executor, types
from random import choice

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = '5674925771:AAE-McW8QREcJ90gSsv2ivWPZEPDr2oEbEM'

bot = Bot(token=BOT_TOKEN)
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
    /emoji = Emoji jo'natish
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


@dp.message_handler(commands=['emoji'])
async def emoji_handler(message: types.Message):
    emojies = ['😇', '🥸', '🤯', '🥶', '🤑']
    await message.answer(f"Siz {choice(emojies)}")


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=set_commands, skip_updates=True)
