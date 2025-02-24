FROM python:3.12-slim

# shell
SHELL ["/bin/bash", "-c"]

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# dependicies
RUN apt-get update && \
    apt-get -qy install gcc libjpeg-dev libpq-dev gettext cron \
    libcairo2 libpango1.0-dev libffi-dev libgirepository1.0-dev \
    libglib2.0-dev shared-mime-info fonts-dejavu nano




WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


RUN mkdir -p /opt/run

COPY  . .

EXPOSE 8019
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
RUN cron -f &


