from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model import Base, Cliente, Profissional


class Agenda(Base):
    __tablename__ = 'agenda'

    id = Column("pk_agenda", Integer, primary_key=True)
    cliente = Column(Integer, ForeignKey("cliente.pk_cliente"), nullable=False)
    profissional = Column(Integer, ForeignKey(
        "profissional.pk_profissional"), nullable=False)
    data_consulta = Column(DateTime, default=datetime.now())

    def __init__(self, cliente: Cliente, profissional: Profissional,
                 data_consulta: Union[DateTime, None] = None):

        self.cliente = cliente
        self.profissional = profissional

        # se não for informada, será o data exata da inserção no banco
        if data_consulta:
            self.data_consulta = data_consulta
