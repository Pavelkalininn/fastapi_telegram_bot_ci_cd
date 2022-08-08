# Телеграм бот с HTTP-API интерфейсом

Бот с помощью наводящих вопросов различает кота от хлеба

## Описание

На вопросы бота можно отвечать следующими фразами независимо от регистра:

    ДА: 'да', 'конечно', 'ага', 'пожалуй'
    НЕТ: 'нет', 'нет, конечно', 'ноуп', 'найн'

![Workflow](https://github.com/Pavelkalininn/fastapi_telegram_bot_ci_cd/actions/workflows/bot_workflow.yml/badge.svg)

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

### Проект доступен по адресу http://51.250.108.40/ или http://kalinin.hopto.org/, все дальнейшие описания запросов сделаны на этих доменах
## Шаблон наполнения env-файла лежит по адресу: 

[infra/example.env](./infra/example.env)

## Запуск проекта:

### Для запуска проекта необходимо в папке infra выполнить команды:
    
    docker-compose up -d --build

после чего будет собран и запущен контейнер


### Для остановки контейнеров необходимо в папке infra выполнить:

     docker-compose down -v


### Документация с примерами запросов доступна по адресу:

    /redoc/

### Для отправки сообщения через телеграм необходимо подключится к боту [Guguruge_test](https://t.me/Guguruge_test_bot) и отправить 

    /start

### Для отправки сообщения через HTTP - API интерфейс нужно перейти по адресу:

    http://kalinin.hopto.org/{telegram_id}/{message}/

где telegram_id - id отправителя (только цифры), а message - само сообщение


### Все сообщения принятые на HTTP API (в том числе и сообщения полученные через бота) сохряняются в БД в структуре:

    | id | telegram_id | text | created_time |

### CI/CD
 После команды git push приложение тестируется на соответствие flake8 и запускаются pytest. 
 При прохождении тестов образы монтируются на docker-hub после чего приложение деплоится на Яндекс облако.
 При положительном результате в телеграм приходит отчёт о выполнении 


Автор: [__Паша Калинин__](https://github.com/Pavelkalininn)
