from sqlalchemy import Column, String, ForeignKey, Integer
from cliente import Cliente
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Juridico(Cliente):
    __tablename__ = 'JURIDICO'
    id = Column('ID', Integer, ForeignKey('CLIENTE.ID'), primary_key=True)
    cnpj = Column('CNPJ', String(20))
    __mapper_args__ = {'polymorphic_identity': 'juridico'}
