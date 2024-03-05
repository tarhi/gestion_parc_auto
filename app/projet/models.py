from app.projet import bd
from sqlalchemy import (
    Integer,
    Column,
    String,
    DateTime,
    ForeignKey,
    Table
)
from sqlalchemy.orm import relationship
from datetime import datetime, time, timedelta



class parc_autos(bd):
    __tablename__ = 'car_table'
    id = Column(Integer, primary_key=True)
    marque = Column(String(10), nullable=False)
    matricule_enregistrer = Column(String(10),nullable=False)
    annee_mise_en_service = Column(String(50), nullable= False)
    client_id = Column(Integer, ForeignKey("client_table.id"))
    km_depart = 0
    client1 = relationship("client", back_populates='car_1' )
    location_id = Column(Integer, ForeignKey('location_table.id'))
    location2 = relationship("location", back_populates='car_2')
    suivi_auto_id = Column(Integer,ForeignKey('suivi_auto_table.id'))
    suivi_auto2 = relationship("suivi_auto",back_populates="car4")
    entretien_id = Column(Integer, ForeignKey('entretien_table.id'))
    entretien_8 = relationship("entretiens", back_populates="car6")

    
    
class client(bd):
    __tablename__='client_table'
    id = Column(Integer, primary_key=True)
    nom = Column(String(50), nullable= False)
    cin = Column(String(10), nullable=False)
    n_permis_conduit = Column(String(10), nullable=False)
    telephone= Column(String(15), nullable= False)
    car_1 = relationship('parc_autos', back_populates='client1')

class location(bd):
    __tablename__= 'location_table'
    id = Column(Integer, primary_key=True)
    matricule1 = Column(String(50),nullable=False)
    client_name = Column(String(50), nullable=False)
    date_location = Column(String(50), nullable=False)
    duree = Column(Integer, nullable=False)
    paiement = Column(String(50), nullable=False)
    prix  = Column(Integer, nullable= False)
    avance = Column(Integer)
    car_2 = relationship('parc_autos',back_populates='location2')

class suivi_auto(bd):
    __tablename__= 'suivi_auto_table'
    id = Column(Integer,primary_key=True)
    matricule2 = Column(String(50), nullable=False)
    type_suivi = Column(String(50), nullable=False)
    date_suivi = Column(String(10), nullable=False)
    car4= relationship("parc_autos",back_populates="suivi_auto2")
    
class entretiens(bd):
    __tablename__='entretien_table'
    id=Column(Integer,primary_key=True)
    matricule3= Column(String(50), nullable=False)
    description= Column(String(100), nullable=False)
    date_entretien = Column(String(50), nullable=False)
    montant = Column(Integer, nullable=False)
    car6 = relationship('parc_autos', back_populates='entretien_8')





    

    
    
    

    


    

    
    