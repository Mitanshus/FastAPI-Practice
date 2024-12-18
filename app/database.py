"""Includes all the modules for dependencies."""

import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()
IS_PROD = os.getenv("IS_PROD")

APP_DB_USERNAME = os.getenv("APP_DB_USERNAME")
APP_DB_IP = os.getenv("APP_DB_IP")
APP_DB_PASSWORD = os.getenv("APP_DB_PASSWORD")
APP_DB_NAME = os.getenv("APP_DB_NAME")
APP_DB_PORT = os.getenv("APP_DB_PORT")

if IS_PROD is False:
    APP_DB_USERNAME = os.getenv("TEST_DB_USERNAME")
    APP_DB_IP = os.getenv("TEST_DB_IP")
    APP_DB_PASSWORD = os.getenv("TEST_DB_PASSWORD")
    APP_DB_NAME = os.getenv("TEST_DB_NAME")
    APP_DB_PORT = os.getenv("TEST_DB_PORT")

# Construct the connection string
URL_DATABASE = os.getenv('DATABASE_URL')

engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base: DeclarativeMeta = declarative_base()


def get_db():
    """Function that manages database session.

    Yiels:
    - db:Session = Database connection
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
