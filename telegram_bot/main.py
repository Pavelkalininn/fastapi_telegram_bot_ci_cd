import logging
import os
import sys
import asyncio
from http import HTTPStatus
from json import JSONDecodeError

import requests
from dotenv import load_dotenv
from requests import RequestException
from telebot.async_telebot import AsyncTeleBot
from telebot import types, ExceptionHandler
from telebot.types import Message

from exceptions import BotException

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

FINAL_PHRASES = [
    'Это кот а не хлеб. Не ешь его!',
    'Это хлеб а не кот! Ешь его!'
]
BUTTONS_VARIANTS = ['Да', 'Нет']
BUTTON_START = ['/start']


class BotExceptionHandler(ExceptionHandler):
    def handle(self, exception):
        logging.error(exception)


def check_tokens():
    """Проверка наличия токена в переменных окружения."""
    if TELEGRAM_TOKEN:
        return True


def get_api_answer(sender_id, message):
    """Возвращает ответ от HTTP API."""
    try:
        api_answer = requests.get(f'http://localhost/{sender_id}/{message}/', timeout=30)
        if api_answer.status_code != HTTPStatus.OK:
            raise BotException(
                f"Пришел некорректный ответ от сервера:"
                f" status_code - {api_answer.status_code}")
        else:
            return api_answer.json()
    except RequestException as error:
        logging.error(error, exc_info=True)
    except JSONDecodeError as error:
        logging.error(error, exc_info=True)


def main():
    """Основная логика работы бота."""
    logging.basicConfig(
        level=logging.INFO,
        handlers=[logging.StreamHandler(sys.stdout), ],
        format=f'%(asctime)s, %(levelname)s, %(message)s, %(name)s')
    bot = AsyncTeleBot(TELEGRAM_TOKEN, exception_handler=ExceptionHandler())
    logging.info('Запуск бота')

    if not check_tokens():
        logging.critical('Отсутствуют переменные окружения.')
        raise BotException('Программа принудительно остановлена.'
                           ' Отсутствуют переменные окружения.')

    @bot.message_handler(commands=['start'])
    async def start(message: Message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*BUTTONS_VARIANTS)
        answer = get_api_answer(message.chat.id, 'start')
        await bot.send_message(message.chat.id, answer, reply_markup=keyboard)

    @bot.message_handler(content_types=['text'])
    async def input_text(message: Message):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        answer = get_api_answer(message.chat.id, message.text)
        buttons = BUTTON_START if answer in FINAL_PHRASES else BUTTONS_VARIANTS
        keyboard.add(*buttons)
        await bot.send_message(message.chat.id, answer, reply_markup=keyboard)

    asyncio.run(bot.polling(none_stop=True, timeout=60, request_timeout=600))


if __name__ == '__main__':
    main()
