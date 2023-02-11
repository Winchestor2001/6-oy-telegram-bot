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


async def show_users_btn(users):
    btn = InlineKeyboardMarkup()
    btn.add(
        *[InlineKeyboardButton(f"{n}", callback_data=f'user:{user[0]}') for n, user in enumerate(users, start=1)]
    )

    return btn


async def user_info_btn(user_id):
    btn = InlineKeyboardMarkup(row_width=1)
    btn.add(
        InlineKeyboardButton("O`chirish", callback_data=f"delete:{user_id}"),
        InlineKeyboardButton("Ortga", callback_data=f"back"),
    )
    return btn


