from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

from tunefind.settings import DB_SETTINGS


def get_engine():
    _db = DB_SETTINGS
    dialet = f"mysql+mysqlconnector://{_db['user']}:{_db['password']}@{_db['host']}:{_db['port']}/{_db['db']}?charset=utf8mb4"
    engine = create_engine(dialet, echo=True)
    return engine


def get_meta():
    meta = MetaData()
    return meta


Base = declarative_base()
meta = get_meta()
engine = get_engine()


# class User(Base):
#     __tablename__ = 'users'
