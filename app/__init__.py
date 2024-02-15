from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy .ext.declarative import declarative_base
app = FastAPI()
engine = create_engine('sqlite:///gg.db')

session_locale= sessionmaker(engine)
base = declarative_base()
def creatsession():
    session = session_locale()
    try:
        yield session
    finally:
        session.close()