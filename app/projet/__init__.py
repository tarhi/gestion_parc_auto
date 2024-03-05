from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy .ext.declarative import declarative_base
from app import bd



app = FastAPI(
    docs_url= "/location_voiture/docs",
    redoc_url = "/location_voiture/redocs",
    title= "Application web pour les locations de voiture",
    description= " Cette application pour assurer la gestion de votre location de voiture",
    version = "2,0",
    openlocation_voiture_url= "location_voiture/.json"
)
engine = create_engine('sqlite:///test.db')

session_locale= sessionmaker(engine)
bd = declarative_base()
def creatsession():
    session = session_locale()
    try:
        yield session
    finally:
        session.close()


from app.projet.models import parc_autos, client, location, suivi_auto, entretiens
from app.projet.models_auth import PostSchema, userSchema, loginuserSchema
bd.metadata.create_all(bind=engine)