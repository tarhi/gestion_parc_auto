from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy .ext.declarative import declarative_base
app = FastAPI(
    docs_url= "/location_voiture/docs",
    redoc_url = "/location_voiture/redocs",
    title= "Application web pour les locations de voiture",
    description= " Cette application pour assurer la gestion des locations de voiture",
    version = "2,0",
    openlocation_voiture_url= "location_voiture/.json",
)
engine = create_engine('sqlite:///test.db')

session_locale= sessionmaker(engine)
base = declarative_base()
def creatsession():
    session = session_locale()
    try:
        yield session
    finally:
        session.close()
from app.models import parc_autos
base.metadata.create_all(bind=engine)