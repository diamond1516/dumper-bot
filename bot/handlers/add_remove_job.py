from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from bot.models import Database
from bot.states import AddDB, RemoveJob
from utils.functions import add_cron_job, remove_cron_job

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
    await state.update_data(port=int(message.text))
    await message.answer('DB interval: ')
    await state.set_state(AddDB.interval)


@router.message(AddDB.interval)
async def handle_project_name(message: Message, state: FSMContext):
    await state.update_data(interval=int(message.text))
    await message.answer('DB interval_type: ')
    await state.set_state(AddDB.interval_type)


@router.message(AddDB.interval_type)
async def handle_project_name(message: Message, state: FSMContext):
    await state.update_data(interval=int(message.text))
    await message.answer('DB api: ')
    await state.set_state(AddDB.api)


@router.message(AddDB.api)
async def handle_project_name(message: Message, session: AsyncSession, state: FSMContext):
    data = await state.get_data()
    data['api'] = message.text
    new_db = Database(**data)
    session.add(new_db)
    await session.commit()
    await message.answer('Raxmat: ')
    await state.clear()

    add_cron_job(
        **data
    )


@router.message(RemoveJob.project_name)
async def handle_project_name(message: Message, session: AsyncSession, state: FSMContext):
    await state.clear()
    res = remove_cron_job(message.text)

    if res:
        await message.answer("Job o'chirildi")
        await state.clear()
        return
    await message.answer("Job o'chirilmadi")
    await state.set_state(RemoveJob.project_name)







