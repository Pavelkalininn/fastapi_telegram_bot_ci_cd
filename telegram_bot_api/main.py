import datetime

import database
import uvicorn
from fastapi import Depends, FastAPI
from models import ModelMessage
from sqlmodel import Session
from starlette.responses import JSONResponse

HELP = """Привет, я могу отличить кота от хлеба! 
Объект перед тобой квадратный?"""

YES = ['да', 'конечно', 'ага', 'пожалуй']
NO = ['нет', 'нет, конечно', 'ноуп', 'найн']
CAT = 'Это кот а не хлеб. Не ешь его!'
BREAD = 'Это хлеб а не кот! Ешь его!'
IS_HAVE_EARS = 'У него есть уши?'
NOT_UNDERSTAND = (
        'Я понимаю только следующие ответы: '
        + '; '.join(YES)
        + '; '
        + '; '.join(NO)
)

database.Model.metadata.create_all(bind=database.engine)
app = FastAPI()

second_message_id = []


def get_db() -> Session:
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


def text_generator(chat_id: int, message: str):
    if message == 'start':
        if chat_id in second_message_id:
            second_message_id.remove(chat_id)
        return HELP
    text = NOT_UNDERSTAND
    yes_in_message = message.lower() in YES
    not_in_message = message.lower() in NO
    if (chat_id in second_message_id
            and (yes_in_message or not_in_message)
    ):
        second_message_id.remove(chat_id)
        text = CAT if yes_in_message else BREAD
    elif yes_in_message:
        second_message_id.append(chat_id)
        text = IS_HAVE_EARS
    elif not_in_message:
        text = CAT
    return text


@app.get("/{telegram_id}/{text}/")
def create_message(telegram_id, text, session: Session = Depends(get_db)):
    if not telegram_id or not telegram_id.isnumeric():
        return {'status': 'Bad Request'}, 400
    elif not text:
        return {'status': 'Text required'}, 400
    telegram_id = int(telegram_id)

    db_message = ModelMessage(
        telegram_id=telegram_id,
        text=text,
        created_time=datetime.datetime.now()
    )
    session.add(db_message)
    session.commit()
    session.refresh(db_message)

    return JSONResponse(text_generator(telegram_id, text), 200)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)
