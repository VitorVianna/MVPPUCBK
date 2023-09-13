from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model import Base


class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column("pk_cliente", Integer, primary_key=True)
    nome = Column(String(140))
    cpf = Column(Integer)
    rg = Column(Integer)
    cep = Column(Integer)
    rua = Column(String(140))
    bairro = Column(String(140))
    cidade = Column(String(140))
    estado = Column(String(140))
    numero = Column(String(140))
    complemento = Column(String(140))
    pais = Column(String(140))
    data_nascimento = Column(DateTime, default=datetime.now())
    sexo = Column(String(1))

    def __init__(self, nome: str, cpf: int, rg: int, cep: int,
                 rua: str, bairro: str, cidade: str, estado: str, numero: str,
                 complemento: str, pais: str, sexo: str, data_nascimento: Union[DateTime, None] = None):

        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.cep = cep
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.numero = numero
        self.complemento = complemento
        self.pais = pais
        self.sexo = sexo

        if data_nascimento:
            self.data_nascimento = data_nascimento
