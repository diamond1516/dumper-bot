#!/bin/bash
set -e

service cron start

alembic upgrade head

python3 main.py
