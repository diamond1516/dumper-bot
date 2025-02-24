import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.utils.callback_answer import CallbackAnswerMiddleware
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from config.settings import SETTINGS, DB_SETTINGS
from middlewares import DbSessionMiddleware
from utils.ui_commands import set_ui_commands
from handlers.routers import __routes__

async def main():
    engine = create_async_engine(url=DB_SETTINGS.database_url, echo=DB_SETTINGS.ECHO)
    sessionmaker = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    bot = Bot(SETTINGS.BOT_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))

    redis = Redis(host=SETTINGS.REDIS_HOST, port=SETTINGS.REDIS_PORT, db=0)

    storage = RedisStorage(redis=redis)

    dp = Dispatcher(storage=storage)
    dp.update.middleware(DbSessionMiddleware(session_pool=sessionmaker))
    dp.callback_query.middleware(CallbackAnswerMiddleware())

    __routes__.register_routes(dp)

    await set_ui_commands(bot)
    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    asyncio.run(main())
