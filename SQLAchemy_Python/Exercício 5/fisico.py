from sqlalchemy import Column, String, ForeignKey, Integer 
from cliente import Cliente
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Fisico(Cliente):
    __tablename__ = 'FISICO'
    id = Column('ID', Integer, ForeignKey('CLIENTE.ID'), primary_key=True)
    cpf = Column('CPF', String(15))
    __mapper_args__ = {'polymorphic_identity': 'fisico'}