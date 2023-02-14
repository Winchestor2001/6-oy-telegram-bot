from aiogram import Dispatcher, Bot, executor, types
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

logging.basicConfig(level=logging.INFO)
BOT_TOKEN = "5674925771:AAE-McW8QREcJ90gSsv2ivWPZEPDr2oEbEM"

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class MyStates(StatesGroup):
    full_name = State()
    age = State()


@dp.message_handler(commands=['start'])
async def bot_start_handler(message: types.Message):
    await message.answer('Salom')


@dp.message_handler(commands=['reg'])
async def bot_reg_handler(message: types.Message):
    await message.answer('Ism va Familiyani kiriting:')
    await MyStates.full_name.set()


@dp.message_handler(state=MyStates.full_name)
async def bot_full_name_state(message: types.Message, state: FSMContext):
    text = message.text
    print('full_name state')

    if len(text.split()) == 2 or len(text.split()) == 3:
        # await state.set_data({'ism': text})
        # await state.update_data({'ism': text})
        data = await state.get_data()
        print(data)
        await state.update_data(ism=text)
        await message.answer("Yoshingizni kiriting:")
        await MyStates.age.set()
    else:
        await message.answer('Ism va Familiyani kiritish shart')


@dp.message_handler(state=MyStates.age)
async def bot_age_state(message: types.Message, state: FSMContext):
    text = message.text

    # print(await state.get_state())
    # print(await state.finish())
    if text.isdigit():
        data = await state.get_data()
        await message.answer(f"Ism: {data['ism']}\n"
                             f"Yosh: {text}")
        # await state.finish()
        await state.reset_state(with_data=False)
    else:
        await message.answer('Yosh son bo`lishi kerak')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

