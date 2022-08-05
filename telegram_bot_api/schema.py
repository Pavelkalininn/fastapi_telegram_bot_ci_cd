from datetime import datetime

from pydantic import BaseModel


class SchemaMessage(BaseModel):
    telegram_id: int
    text: str = None
    created_time: datetime

    class Config:
        orm_mode = True
