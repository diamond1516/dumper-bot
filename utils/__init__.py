from datetime import datetime
from zoneinfo import ZoneInfo
from bot.config_reader import SETTINGS


def now(timezone: str = SETTINGS.TIME_ZONE):
    return datetime.now(ZoneInfo(timezone))

