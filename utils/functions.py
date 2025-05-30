from typing import Literal
from typing import Optional

from crontab import CronTab

from config.settings import SETTINGS


def add_cron_job(
        project_name,
        name,
        password,
        user,
        host,
        port: int,
        api: str,
        interval: int,
        interval_type: Literal['hour', 'day', 'week', 'month', 'minute'] = 'minute',
):
    cron = CronTab(user=True)
    command = f'{SETTINGS.SCRIPT_VENV_PATH}/python3 {SETTINGS.SCRIPT_PATH}/script.py {project_name} {name} {password} {user} {host} {port} {api}'

    job = cron.new(command=command, comment=f'pg_dump_jobs_{project_name}')

    if interval_type == "hour":
        job.minute.on(0)
        job.hour.every(interval)
    elif interval_type == "day":
        job.minute.on(0)
        job.hour.on(0)
        job.day.every(interval)
    elif interval_type == "week":
        job.minute.on(0)
        job.hour.on(0)
        job.dow.every(interval)
    elif interval_type == "month":
        job.minute.on(0)
        job.hour.on(0)
        job.day.on(1)
        job.month.every(interval)
    elif interval_type == "minute":
        assert interval <= 59, 'The interval must be in hour, day, month'
        job.minute.every(interval)

    cron.write()
    return f"Cron job added for {project_name} at interval {interval} {interval_type}"


def remove_cron_job(project_name):
    cron = CronTab(user=True)

    jobs_removed = False
    for job in cron:
        if job.comment == f'pg_dump_jobs_{project_name}':
            cron.remove(job)
            jobs_removed = True

    cron.write()

    return jobs_removed


def clear_cron_job():
    cron = CronTab(user=True)
    jobs_to_remove = [job for job in cron if job.comment.startswith("pg_dump_jobs_")]

    for job in jobs_to_remove:
        cron.remove(job)

    cron.write()
    return f"{len(jobs_to_remove)} ta cron job o‘chirildi."


def set_custom_cron_job(
        project_name: str,
        name: str,
        password: str,
        user: str,
        host: str,
        port: int,
        api: str,
        minute: Optional[str] = '*',  # 0-59 yoki '*'
        hour: Optional[str] = '*',  # 0-23 yoki '*'
        day: Optional[str] = '*',  # 1-31 yoki '*'
        month: Optional[str] = '*',  # 1-12 yoki '*'
        weekday: Optional[str] = '*',  # 0-6 (Yakshanba=0) yoki '*'
):
    cron = CronTab(user=True)
    command = f'{SETTINGS.SCRIPT_VENV_PATH}/python3 {SETTINGS.SCRIPT_PATH}/script.py {project_name} {name} {password} {user} {host} {port} {api}'

    job = cron.new(command=command, comment=f'pg_dump_jobs_{project_name}')
    job.setall(f'{minute} {hour} {day} {month} {weekday}')
    cron.write()
    return f"Cron job added for {project_name} with schedule {minute} {hour} {day} {month} {weekday}"
