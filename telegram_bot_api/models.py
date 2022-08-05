from sqlalchemy import Column, Integer, String, DateTime

from database import Model


class ModelMessage(Model):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(Integer)
    text = Column(String)
    created_time = Column(DateTime)

