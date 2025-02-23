from aiogram import Bot
from aiogram.types import BotCommandScopeAllPrivateChats, BotCommand


async def set_ui_commands(bot: Bot):
    """
    Sets bot commands in UI
    :param bot: Bot instance
    """
    commands = [
        BotCommand(command="play", description="Start new game"),
        BotCommand(command="list", description="View databases"),
        BotCommand(command="add", description="Add database"),
        BotCommand(command="remove", description="Remove database"),
        BotCommand(command="clear", description="Clear databases"),
    ]
    await bot.set_my_commands(
        commands=commands,
        scope=BotCommandScopeAllPrivateChats()
    )
