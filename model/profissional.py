from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union
import json
from model import Base


class Profissional(Base):
    __tablename__ = 'profissional'

    id = Column("pk_profissional", Integer, primary_key=True)
    nome = Column(String(140))
    crm = Column(String(15))

    # Definição do relacionamento entre o produto e o comentário.
    # Essa relação é implicita, não está salva na tabela 'produto',
    # mas aqui estou deixando para SQLAlchemy a responsabilidade
    # de reconstruir esse relacionamento.
    # comentarios = relationship("Comentario")

    def __init__(self, nome: str, crm: str):

        self.nome = nome
        self.crm = crm

    def listar_profissionais(self):
        return self
