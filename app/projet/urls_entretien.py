from app.projet import app, creatsession
from app.projet.models import entretiens
from fastapi import Depends,status, Response
from sqlalchemy.orm import Session
from datetime import datetime,date


@app.get('/entretien/',tags=["Entretien des voitures"])
def afficher_tous_entretien(session:Session = Depends(creatsession)):
    entretien_1 = session.query(entretiens).all()
    return {"la liste des opérations de location est: ":entretien_1}

@app.get('/entretien{id}', status_code=status.HTTP_200_OK,tags=["Entretien des voitures"])
def selectionner_id_entretien(id:str,res:Response,session:Session = Depends(creatsession)):
    entretien1 = session.query(entretiens).filter_by(id=id).first()
    if entretien1 == None:
        res.status_code= status.HTTP_404_NOT_FOUND
        return {f"{id}: id does not exist"}
    return {"id sélectionner est pour la voiture: ":entretien1}

@app.post('/entretien/',status_code=status.HTTP_201_CREATED,tags=["Entretien des voitures"])
def creer_nouveau_entretien(matricule3:str,description:str,date_entretien:str,montant:int,session:Session = Depends(creatsession)):
    entretien_ = entretiens(matricule3=matricule3,description=description,date_entretien=date_entretien,montant=montant)
    session.add(entretien_)
    session.commit()
    session.refresh(entretien_)
    return {"la prestation est bien crée: ":entretien_}