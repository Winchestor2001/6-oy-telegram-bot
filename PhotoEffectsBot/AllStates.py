from aiogram.dispatcher.filters.state import StatesGroup, State


class UserStates(StatesGroup):
    get_photo = State()
