from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove


remove = ReplyKeyboardRemove()


async def menu_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.row("🖼 Rasimga Joziba berish")
    btn.row("📊 Statistika", "👩‍💻 Biz bilan aloqa")
    return btn


