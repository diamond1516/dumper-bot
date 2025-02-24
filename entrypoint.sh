#!/bin/bash
set -e

service cron start

python3 main.py
