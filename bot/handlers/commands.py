import sqlalchemy as sa
from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from bot.models import Database
from bot.states import AddDB

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
        await message.answer(', '.join([database.project_name for database in databases]))





@router.message(Command("add"))
async def cmd_add(message: Message, session: AsyncSession, state: FSMContext):
    await message.answer('Project nomi:')
    await state.set_state(AddDB.project_name)




@router.message(Command("remove"))
async def cmd_remove(message: Message, session: AsyncSession):
    pass


@router.message(Command("clear"))
async def cmd_clear(message: Message, session: AsyncSession):
    pass