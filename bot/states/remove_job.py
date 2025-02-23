from aiogram.fsm.state import StatesGroup, State


class RemoveJob(StatesGroup):
    project_name = State()
