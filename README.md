# Телеграм бот с HTTP-API интерфейсом

Бот с помощью наводящих вопросов различает кота от хлеба

## Описание

На вопросы бота можно отвечать следующими фразами независимо от регистра:

    ДА: 'да', 'конечно', 'ага', 'пожалуй'
    НЕТ: 'нет', 'нет, конечно', 'ноуп', 'найн'

![Workflow](https://github.com/Pavelkalininn/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## Технологии

    aiohttp
    pyTelegramBotAPI
    python-dotenv
    fastapi
    psycopg2==2.9.3
    pydantic==1.9.1
    python-dotenv==0.20.0
    sniffio==1.2.0
    SQLAlchemy==1.4.39
    starlette==0.19.1
    typing_extensions==4.3.0
    uvicorn==0.18.2
    zipp==3.8.1
    sqlmodel
    alembic==1.8.1

### Проект доступен по адресу http://51.250.108.40 или http://kalinin.hopto.org/, все дальнейшие описания запросов сделаны на этих доменах
## Шаблон наполнения env-файла лежит по адресу: 

[infra/example.env](./infra/example.env)

## Запуск проекта:

### Для запуска проекта необходимо в папке infra выполнить команды:
    
    docker-compose up -d --build

после чего будет собран и запущен контейнер


### Для остановки контейнера необходимо в папке infra выполнить:

     docker-compose down -v


## Документация с примерами запросов доступна по адресу:

    /redoc/



Автор: [__Паша Калинин__](https://github.com/Pavelkalininn)
