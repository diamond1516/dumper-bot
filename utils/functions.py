from crontab import CronTab
from config.settings import SETTINGS
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
    command = f'{SETTINGS.SCRIPT_VENV_PATH}/bin/python {SETTINGS.SCRIPT_PATH}/script.py {project_name} {name} {password} {user} {host} {port} {api}'

    job = cron.new(command=command, comment=f'pg_dump_jobs_{project_name}')

    if interval_type == "hour":
        job.minute.on(0)
    elif interval == "day":
        job.minute.on(0)
        job.hour.on(0)
    elif interval_type == "week":
        job.minute.on(0)
        job.hour.on(0)
        job.dow.on(0)
    elif interval_type == "month":
        job.minute.on(0)
        job.hour.on(0)
        job.day.on(1)
    elif interval_type == "minute":
        assert interval <= 59 , 'The interval must be in hour, day, month'
        job.minute.every(interval)

    cron.write()
    return f"Cron job added for {project_name} at interval {interval}"




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





