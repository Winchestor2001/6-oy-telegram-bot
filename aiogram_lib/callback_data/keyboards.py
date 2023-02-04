from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


start_btn = InlineKeyboardMarkup()
start_btn.add(
    InlineKeyboardButton(text="👍", callback_data="like"),
    InlineKeyboardButton(text="👎", callback_data="dislike"),
)

random_img_btn = InlineKeyboardMarkup(row_width=2)
random_img_btn.add(
    InlineKeyboardButton(text="❤️", callback_data="like"),
    InlineKeyboardButton(text="🦅", callback_data="fast"),
    InlineKeyboardButton(text="Next", callback_data="next"),
)

plus_mines_btn = InlineKeyboardMarkup()
plus_mines_btn.add(
    InlineKeyboardButton(text="+", callback_data="plus"),
    InlineKeyboardButton(text="-", callback_data="mines"),
)



