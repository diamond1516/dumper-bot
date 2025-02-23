from crontab import CronTab
from bot.config_reader import SETTINGS
from typing import Literal

def add_cron_job(
        project_name,
        name,
        password,
        user,
        host,
        port: int,
        api: str,
        interval: int,
        interval_type: Literal['hour', 'day', 'month', 'minute'] = 'minute',
):
    cron = CronTab(user=True)

    command = f'python3 {SETTINGS.SCRIPT_PATH}/script.py {project_name} {name} {password} {user} {host} {port} {api}'

    job = cron.new(command=command, comment=project_name)

    if interval == "hour":
        job.minute.on(0)
    elif interval == "day":
        job.minute.on(0)
        job.hour.on(0)
    elif interval == "week":
        job.minute.on(0)
        job.hour.on(0)
        job.dow.on(0)
    elif interval == "month":
        job.minute.on(0)
        job.hour.on(0)
        job.day.on(1)
    elif interval == "minute":
        assert interval >= 59 , 'The interval must be in hour, day, month'
        job.minute.every(interval)

    cron.write()
    return f"Cron job added for {project_name} at interval {interval}"



