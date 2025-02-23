from datetime import datetime
from zoneinfo import ZoneInfo
from config.settings import SETTINGS


def now(timezone: str = SETTINGS.TIME_ZONE):
    return datetime.now(ZoneInfo(timezone))

