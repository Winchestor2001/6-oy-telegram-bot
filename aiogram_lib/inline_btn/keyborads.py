from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


start_menu_btn = InlineKeyboardMarkup(row_width=1)
start_menu_btn.add(
    InlineKeyboardButton(text="Salom 1", callback_data='send_salom'),
    InlineKeyboardButton(text="Paka 2", callback_data='send_paka'),
    InlineKeyboardButton(text="GitHub", url="https://www.github.com"),
)
