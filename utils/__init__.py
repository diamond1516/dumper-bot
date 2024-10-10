from datetime import datetime
from zoneinfo import ZoneInfo
from bot.config_reader import config


def now(timezone: str = config.TIME_ZONE):
    return datetime.now(ZoneInfo(timezone))

