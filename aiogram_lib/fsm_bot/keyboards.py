from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, \
    ReplyKeyboardRemove

remove_btn = ReplyKeyboardRemove()


async def gander_options_btn():
    btn = InlineKeyboardMarkup(row_width=2)
    btn.add(
        InlineKeyboardButton(text='Erkak', callback_data='gander:erkak'),
        InlineKeyboardButton(text='Ayol', callback_data='gander:ayol')
    )
    return btn


async def send_phone_number_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.add(
        KeyboardButton("Telefon raqam", request_contact=True)
    )
    return btn

