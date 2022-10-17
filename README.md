# Telegram bot with HTTP API interface

The bot with the help of leading questions distinguishes the cat from the bread

## Description

The bot's questions can be answered with the following phrases regardless of the case:

    ДА: 'да', 'конечно', 'ага', 'пожалуй', 'д', 'y', 'yes', 'ад', 'lf', 'нуы', 'ys'
    НЕТ: 'нет', 'нет, конечно', 'ноуп', 'найн', 'no', 'n', 'н', 'нт', 'не', 'ytn',
    'тщ',

![Workflow](https://github.com/Pavelkalininn/fastapi_telegram_bot_ci_cd/actions/workflows/bot_workflow.yml/badge.svg)

## Technologies

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

## The template for filling the env file is located at:

[infra/example.env](./infra/example.env)

## Run:

### To run the project, run the following commands in the infra folder:
    
    docker-compose up -d --build
    
after that, the container will be assembled and launched


### To stop containers, you need to run in the infra folder:

     docker-compose down -v


### Documentation with sample requests is available at:

    /redoc/

### To send a message via telegram, you need to connect to the bot [Guguruge_test](https://t.me/Guguruge_test_bot ) and send

    /start

### To send a message via the HTTP API , go to:

    https://kalinin.hopto.org/{telegram_id}/{message}/

where telegram_id is the sender's id (digits only), and message is the message itself


### All messages received on the HTTP API (including messages received through the bot) are stored in the database in the structure:

    | id | telegram_id | text | created_time |

### CI/CD
After the git push command, the application is tested for compliance with flake8 and pytest runs.
When passing the tests, the images are mounted on the docker-hub, after which the application is deployed to Yandex cloud.
If the result is positive, the telegram receives a report on the implementation


Author: [__Pavel Kalinin__](https://github.com/Pavelkalininn)
