import asyncio
import logging
from aiogram import Dispatcher, Bot, executor, types
from keyborads import start_menu_btn

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
    await message.answer_chat_action('typing')
    await message.answer("Assalomu aleykum", reply_markup=start_menu_btn)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=set_commands, skip_updates=True)

