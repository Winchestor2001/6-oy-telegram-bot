import logging
from aiogram import Dispatcher, Bot, executor, types

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


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=set_commands, skip_updates=True)
