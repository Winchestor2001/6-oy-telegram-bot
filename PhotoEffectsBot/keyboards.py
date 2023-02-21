from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


remove = ReplyKeyboardRemove()


async def menu_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.row("🖼 Rasimga Joziba berish")
    btn.row("📊 Statistika", "👩‍💻 Biz bilan aloqa")
    return btn


async def effects_btn(data):
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn.add(
        *[KeyboardButton(item[0]) for item in data]
    )

    return btn

