import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.utils.callback_answer import CallbackAnswerMiddleware
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from bot.config_reader import SETTINGS
from bot.middlewares import DbSessionMiddleware
from bot.ui_commands import set_ui_commands
from bot.routers import __routes__


async def main():
    engine = create_async_engine(url=SETTINGS.DB_URL, echo=True)
    sessionmaker = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    bot = Bot(SETTINGS.BOT_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))

    # Setup dispatcher and bind routers to it
    dp = Dispatcher()
    dp.update.middleware(DbSessionMiddleware(session_pool=sessionmaker))
    # Automatically reply to all callbacks
    dp.callback_query.middleware(CallbackAnswerMiddleware())

    # Register handlers
    __routes__.register_routes(dp)

    # Set bot commands in UI
    await set_ui_commands(bot)
    await bot.delete_webhook(drop_pending_updates=True)

    # Run bot
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())
