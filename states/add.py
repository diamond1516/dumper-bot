from aiogram.fsm.state import StatesGroup, State


class AddDB(StatesGroup):
    project_name = State()
    name = State()
    password = State()
    user = State()
    host = State()
    port = State()
    interval = State()
    interval_type = State()
    api = State()
