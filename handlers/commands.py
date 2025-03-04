import sqlalchemy as sa
from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from models import Database
from states import AddDB, RemoveJob
from utils.functions import clear_cron_job, add_cron_job

router = Router(name="commands-router")


@router.message(CommandStart())
async def cmd_start(message: Message):
    """
    Handles /start command
    :param message: Telegram message with "/start" text
    """
    await message.answer(
        "Hi there! This is a simple clicker bot. Tap on green ball, but don't tap on red ones!\n"
        "If you tap a red ball, you'll have to start over.\n\n"
        "Enough talk. Just tap /play and have fun!"
    )


@router.message(Command("list"))
async def cmd_list(message: Message, session: AsyncSession):
    """
    Handles /play command
    :param message: Telegram message with "/play" text
    :param session: DB connection session
    """
    stmt = sa.select(Database).order_by(Database.id.desc())
    result = await session.execute(stmt)
    databases = result.scalars().all()
    if databases:
        msg = ''

        for database in databases:
            msg += (f'Project: <code>{database.project_name}</code>\n'
                    f'DB name: <code>{database.name}</code>\n'
                    f'DB pass: <code>{database.password}</code>\n'
                    f'DB user: <code>{database.user}</code>\n'
                    f'DB host: <code>{database.host}</code>\n'
                    f'DB port: <code>{database.port}</code>\n'
                    f'Interval: {database.interval} {database.interval_type}\n'
                    f'Dump API: {database.api}\n\n\n')

        await message.answer(msg)
    else:
        await message.answer('No databases found')




@router.message(Command("add"))
async def cmd_add(message: Message, session: AsyncSession, state: FSMContext):
    await message.answer('Project nomi:')
    await state.set_state(AddDB.project_name)




@router.message(Command("remove"))
async def cmd_remove(message: Message, session: AsyncSession, state: FSMContext):
    await message.answer('Project nomi:')
    await state.set_state(RemoveJob.project_name)



@router.message(Command("clear"))
async def cmd_clear(message: Message, session: AsyncSession):
    msg = clear_cron_job()
    await message.answer(msg)


@router.message(Command("restart"))
async def cmd_restart(message: Message, session: AsyncSession, state: FSMContext):
    msg = clear_cron_job()
    await message.answer(msg)
    stmt = sa.select(Database).order_by(Database.id.desc())
    result = await session.execute(stmt)
    databases = result.scalars().all()
    count = len(databases)
    if databases:
        for database in databases:
            add_cron_job(
                project_name=database.project_name,
                name=database.name,
                password=database.password,
                user=database.user,
                host=database.host,
                port=database.port,
                api=database.api,
                interval=database.interval,
                interval_type=database.interval_type,
            )

        await message.answer(f'{count} cron jobs restarted.')
    else:
        await message.answer('No cron jobs restarted.')




