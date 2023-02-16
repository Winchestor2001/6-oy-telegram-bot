from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def gander_options_btn():
    btn = InlineKeyboardMarkup(row_width=2)
    btn.add(
        InlineKeyboardButton(text='Erkak', callback_data='gander:erkak'),
        InlineKeyboardButton(text='Ayol', callback_data='gander:ayol')
    )
    return btn


