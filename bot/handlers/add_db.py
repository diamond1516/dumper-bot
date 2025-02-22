from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from bot.states import AddDB

router = Router(
    name='Add Database',
)


@router.message(AddDB.project_name)
async def handle_project_name(message: Message, state: FSMContext):
    await state.update_data(project_name=message.text)
    await message.answer('DB name: ')
    await state.set_state(AddDB.name)


@router.message(AddDB.name)
async def handle_project_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('DB password: ')
    await state.set_state(AddDB.password)


@router.message(AddDB.password)
async def handle_project_name(message: Message, state: FSMContext):
    await state.update_data(password=message.text)
    await message.answer('DB username: ')
    await state.set_state(AddDB.user)


@router.message(AddDB.user)
async def handle_project_name(message: Message, state: FSMContext):
    await state.update_data(user=message.text)
    await message.answer('DB host: ')
    await state.set_state(AddDB.host)


@router.message(AddDB.host)
async def handle_project_name(message: Message, state: FSMContext):
    await state.update_data(host=message.text)
    await message.answer('DB port: ')
    await state.set_state(AddDB.port)


@router.message(AddDB.port)
async def handle_project_name(message: Message, state: FSMContext):
    await state.update_data(port=message.text)
    await message.answer('DB interval: ')
    await state.set_state(AddDB.interval)


@router.message(AddDB.interval)
async def handle_project_name(message: Message, state: FSMContext):
    await state.update_data(interval=message.text)
    await message.answer('DB api: ')
    await state.set_state(AddDB.api)


@router.message(AddDB.api)
async def handle_project_name(message: Message, session: AsyncSession, state: FSMContext):
    await state.update_data(api=message.text)



    await message.answer('Raxmat: ')



