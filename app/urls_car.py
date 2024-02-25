from app import app, creatsession
from app.models import parc_autos
from fastapi import Depends,status, Response
from sqlalchemy.orm import Session

@app.get('/car/', tags=["parc_automobile"])
def afficher_parc_autos(session:Session = Depends(creatsession)):
    parc = session.query(parc_autos).all()
    return {"le parc auto se compose des voitures: ":parc}

@app.get('/car{id}', status_code=status.HTTP_200_OK, tags=["parc_automobile"])
def selectionner_auto(id:str,res:Response,session:Session = Depends(creatsession)):
    parc1 = session.query(parc_autos).filter_by(id=id).first()
    if parc1 == None:
        res.status_code = status.HTTP_404_NOT_FOUND
        return {f" ID: {id} id does not exist"}
    return {"id sélectionner est pour la voiture: ":parc1}


@app.post('/car/',status_code=status.HTTP_201_CREATED, tags=["parc_automobile"])
def creer_auto(marque:str,matricule_enregistrer:str,annee_mise_en_service:str,session:Session = Depends(creatsession)):
    car = parc_autos(marque=marque,matricule_enregistrer=matricule_enregistrer, annee_mise_en_service= annee_mise_en_service)
    session.add(car)
    session.commit()
    session.refresh(car)
    return {"id crée est: ":car}

@app.put('/car/{id}', tags=["parc_automobile"])
def modifier_auto(id:int, marque:str,matricule_enregistrer:str,annee_mise_en_service:str,session:Session = Depends(creatsession)):
    car2 = session.query(parc_autos).filter_by(id=id).first()
    if car2 == None:
        return("id does not exist")
    session.marque = marque
    session.annee_mise_en_service = annee_mise_en_service
    session.commit()
    return {"id est bien modifié": car2}

@app.patch('/car/{id}', tags=["parc_automobile"])
def modifier_auto(id:int, marque:str,matricule_enregistrer:str,annee_mise_en_service:str,session:Session = Depends(creatsession)):
    car3 = session.query(parc_autos).filter_by(id=id).first()
    if car3 == None:
        return("id does not exist")
    if marque:
        car3.marque = marque
    if annee_mise_en_service:
        car3.annee_mise_en_service = annee_mise_en_service
    session.commit()
    session.refresh(car3)
    return {"le champs est bien modifié": car3}

@app.delete('/car/{id}', tags=["parc_automobile"])
def supprimer_auto(id:int,session:Session = Depends(creatsession)):
    car4 = session.query(parc_autos).filter_by(id=id).delete()
    if car4 == None:
        return("id does not exist")
    session.delete(car4)
    session.commit()
    return("ID car deleted")




    

    
   



