FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app/telegram_bot_api/

COPY requirements.txt .
RUN python -m pip install --upgrade pip && pip3 install -r ./requirements.txt --no-cache-dir

COPY .. .

EXPOSE 80