from database import Model
from sqlalchemy import Column, DateTime, Integer, String


class ModelMessage(Model):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(Integer)
    text = Column(String)
    created_time = Column(DateTime)
