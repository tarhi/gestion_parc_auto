from app import base
from sqlalchemy import (
    Integer,
    Column,
    String,
    DateTime
)
from sqlalchemy.orm import relationship
from datetime import datetime
class parc(base):
    __tablename__ = 'parc'
    id = Column(Integer,primary_key=True)
    annee = Column(DateTime,)