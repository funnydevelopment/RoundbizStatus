FROM python:3.11-slim-buster

ENV PYTHONUNBUFFERED=1

COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

WORKDIR /app
COPY . .