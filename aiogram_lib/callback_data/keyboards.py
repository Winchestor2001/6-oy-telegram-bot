from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


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


menu_btn = ReplyKeyboardMarkup(resize_keyboard=True)
menu_btn.row("Ishchilar", "Maxsulotlar")


back_btn = InlineKeyboardMarkup()
back_btn.add(InlineKeyboardButton(text="Ortga", callback_data="back_ishchilar"))


async def ishchilar_btn(data):
    btn = InlineKeyboardMarkup(row_width=1)
    for ishchi in data:
        btn.add(
            InlineKeyboardButton(text=f"{ishchi['name']}", callback_data=f"ishchi_{ishchi['id']}")
        )

    return btn


