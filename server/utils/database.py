import logging
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from settings import settings

# connect to the database
logging.debug(f"db connection string is: {settings.sqlalchemy_url}")
#engine = create_engine(settings.sqlalchemy_url, connect_args={"check_same_thread": False})
engine = create_engine(settings.sqlalchemy_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
