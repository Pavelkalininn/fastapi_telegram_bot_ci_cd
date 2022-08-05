import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(os.environ.get(
    "DATABASE_URL",
    default='sqlite:///db_file.db')
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Model = declarative_base()
