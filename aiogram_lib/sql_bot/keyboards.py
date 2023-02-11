from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


async def menu_btn(text):
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.add(
        KeyboardButton(text)
    )
    return btn


async def select_lang_btn():
    btn = InlineKeyboardMarkup(row_width=2)
    btn.add(
        InlineKeyboardButton("🇷🇺", callback_data="lang:ru"),
        InlineKeyboardButton("🇺🇿", callback_data="lang:uz")
    )
    return btn




