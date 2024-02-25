from app import app, creatsession
from app.models import suivi_auto
from fastapi import Depends, status, Response, HTTPException
from sqlalchemy.orm import Session


@app.get('/suivi_auto/',tags=["suivi des voitures"])
def afficher_all_suivi(session:Session = Depends(creatsession)):
    suivi_autos = session.query(suivi_auto).all()
    return {"la liste des opérations de location est: ":suivi_autos}

@app.get('/suivi_auto{id}', status_code=status.HTTP_200_OK,tags=["suivi des voitures"])
def selectionner_id_suivi(id:str, res:Response , session:Session = Depends(creatsession)):
    suivi_auto1 = session.query(suivi_auto).filter_by(id=id).first()
    if suivi_auto1 == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID: {id} does not exist")
        # return{f"ID: {id} does not exist"}
    return {"id sélectionner est pour la voiture: ":suivi_auto1}

@app.post('/suivi_auto/', status_code=status.HTTP_201_CREATED,tags=["suivi des voitures"])
def creer_un_suivi(matricule2:str,type_suivi:str,date_suivi=str,session:Session = Depends(creatsession)):
    suivi_auto_ = suivi_auto(matricule2=matricule2,type_suivi=type_suivi,date_suivi=date_suivi)
    session.add(suivi_auto_)
    session.commit()
    session.refresh(suivi_auto_)
    return {"la prestation est bien crée: ":suivi_auto_}