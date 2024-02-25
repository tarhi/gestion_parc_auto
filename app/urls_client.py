from app import app, creatsession
from app.models import client
from fastapi import Depends, status, Response, HTTPException
from sqlalchemy.orm import Session


@app.get('/client/', tags=["Base clients"])
def afficher_all_client(id:str,session:Session = Depends(creatsession)):
    client_all = session.query(client).all()
    return {"la liste des clients est: ": client_all}

@app.get('/client/{id}', status_code=status.HTTP_200_OK, tags=["Base clients"])
def afficher_client_id(id:str,res: Response, nom:str,cin:str,n_permis_conduit:str,telephone:str,session:Session = Depends(creatsession)):
    client_id = session.query(client).filter_by(id=id).first()
    if client_id == None:
        res.status_code=status.HTTP_404_NOT_FOUND
        return {f"{id}: id customer does not exist"}
    return {"le client sélectionné est: ": client_id}


@app.post('/client/',status_code=status.HTTP_201_CREATED, tags=["Base clients"])
def creer_nouveau_client(nom:str,cin:str,n_permis_conduit:str,telephone:str,session:Session = Depends(creatsession)):
    client_ = client(nom=nom,cin=cin,n_permis_conduit=n_permis_conduit,telephone=telephone)
    session.add(client_)
    session.commit()
    session.refresh(client_)
    return {"le client est bien crée: ":client_}

@app.put('/client/{id}', tags=["Base clients"])
def modifier_all_client(id:int,nom:str,cin:str,n_permis_conduit:str,telephone:str,session:Session = Depends(creatsession)):
    client_2 = session.query(client).filter_by(id=id).first()
    if client_2 == None:
        return("customer does not exist")
    session.nom = nom
    session.telephone = telephone
    session.cin = cin
    session.n_permis_conduit = n_permis_conduit
    session.commit()
    return client_2

@app.patch('/client/{id}', tags=["Base clients"])
def modifier_id_client(id:int,nom:str,cin:str,n_permis_conduit:str,telephone:str,session:Session = Depends(creatsession)):
    client_4 = session.query(client).filter_by(id=id).first()
    if client_4 == None:
        return("customer does not exist")
    if nom:
        session.nom = nom
    if telephone:
        session.telephone = telephone
    if cin:
        session.cin = cin
    if n_permis_conduit:
        session.n_permis_conduit = n_permis_conduit
    session.commit()
    session.refresh(client_4)
    return client_4

@app.delete('/client/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Base clients"])
def supprimer_id_client(id:int,res:Response,session:Session = Depends(creatsession)):
    client_3 = session.query(client).filter_by(id=id)
    if client_3.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=" ID does not exist")
    client_3.delete()
    session.commit()
    return ("client deleted")