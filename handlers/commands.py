from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from config.settings import SETTINGS
from models import Database
from states import AddDB, RemoveJob
from utils.functions import clear_cron_job, add_cron_job, set_custom_cron_job

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


import asyncio
import shlex
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession
import sqlalchemy as sa

router = Router()


@router.message(Command("get"))
async def cmd_get(message: Message, session: AsyncSession):
    parts = message.text.split(maxsplit=1)
    word = parts[1] if len(parts) > 1 else None

    if not word:
        return await message.answer("Iltimos, so‘zni kiriting: `/get <name>`")

    stmt = sa.select(Database).where(Database.project_name == word).limit(1)
    result = await session.execute(stmt)
    database: Database = result.scalar_one_or_none()

    if not database:
        return await message.answer(f"“{word}” nomli baza topilmadi.")

    command = (
        f"{SETTINGS.SCRIPT_VENV_PATH}/python3 "
        f"{SETTINGS.SCRIPT_PATH}/script.py "
        f"{shlex.quote(database.project_name)} "
        f"{shlex.quote(database.name)} "
        f"{shlex.quote(database.password)} "
        f"{shlex.quote(database.user)} "
        f"{shlex.quote(database.host)} "
        f"{shlex.quote(str(database.port))} "
        f"{shlex.quote(database.api)}"
    )

    await message.answer(f"Komanda ishga tushirilmoqda:\n```\n{command}\n```")

    process = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()

    if stdout:
        await message.answer(f"✅ Natija:\n<pre>{stdout.decode().strip()}</pre>")
    if stderr:
        await message.answer(f"⚠️ Xatolik:\n<pre>{stderr.decode().strip()}</pre>")


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
            if database.interval_type != 'schedule':
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
            else:
                set_custom_cron_job(
                    project_name=database.project_name,
                    name=database.name,
                    password=database.password,
                    user=database.user,
                    host=database.host,
                    port=database.port,
                    api=database.api,
                    schedule=database.interval,
                )

        await message.answer(f'{count} cron jobs restarted.')
    else:
        await message.answer('No cron jobs restarted.')
