from app import app, creatsession
from app.models import location
from fastapi import Depends, status, Response
from sqlalchemy.orm import Session


@app.get('/location/', tags= ["Prestation de service"])
def afficher_location(session:Session = Depends(creatsession)):
    location_1 = session.query(location).all()
    return {"la liste des opérations de location est: ":location_1}

@app.get('/location{id}', status_code=status.HTTP_200_OK, tags= ["Prestation de service"])
def selectionner_location(id:str,res: Response, session:Session = Depends(creatsession)):
    location1 = session.query(location).filter_by(id=id).first()
    if location1 == None :
        res.status_code = status.HTTP_404_NOT_FOUND
        return{f"ID: {id} id does not exist"}
    return {"id sélectionner est pour la voiture: ":location1}

@app.post('/location/', status_code=status.HTTP_201_CREATED, tags= ["Prestation de service"])
def creer_nouvelle_location(matricule1:str,client_name:str,date_location:str,duree:int,paiement:str,prix:int,avance:int,session:Session = Depends(creatsession)):
    location_ = location(matricule1=matricule1,client_name=client_name,date_location=date_location,duree=duree,paiement=paiement,prix=prix,avance=avance)
    session.add(location_)
    session.commit()
    session.refresh(location_)
    return {"la prestation est bien crée: ":location_}