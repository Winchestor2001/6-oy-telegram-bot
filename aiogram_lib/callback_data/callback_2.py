from aiogram import Dispatcher, Bot, executor, types
import logging
from keyboards import menu_btn, ishchilar_btn

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = '5674925771:AAE-McW8QREcJ90gSsv2ivWPZEPDr2oEbEM'

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

ishchilar = [
    {
        'id': 1,
        'name': 'Baxodir',
        'lavozim': 'Qoravul',
    },
    {
        'id': 2,
        'name': 'Ozodbek',
        'lavozim': 'Oshpaz',
    },
    {
        'id': 3,
        'name': 'Suhrobjon',
        'lavozim': 'Mantyor',
    },
    {
        'id': 4,
        'name': 'Axmadbek',
        'lavozim': 'Ofitsiant',
    },
    {
        'id': 5,
        'name': 'Odiljon',
        'lavozim': 'Buxgalter',
    },
]


async def on_startup(dp: Dispatcher):
    await dp.bot.set_my_commands(
        [
            types.BotCommand('start', 'Ishga tushurish'),
        ]
    )


@dp.message_handler(commands=['start'])
async def bot_start_handler(message: types.Message):
    await message.delete()
    await message.answer("Salom", reply_markup=menu_btn)


@dp.message_handler(text='Ishchilar')
async def ishchilar_handler(message: types.Message):
    btn = await ishchilar_btn(ishchilar)
    await message.answer("Ishchilar:", reply_markup=btn)


@dp.callback_query_handler(text_contains='ishchi_')
async def ishchi_callback(callback: types.CallbackQuery):
    await callback.answer()
    ishchi_id = int(callback.data.split("_")[-1])
    for i in ishchilar:
        if i['id'] == ishchi_id:
            print(i['name'], i['lavozim'])
            break


@dp.message_handler(text='Maxsulotlar')
async def maxsulotlar_handler(message: types.Message):
    print(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
