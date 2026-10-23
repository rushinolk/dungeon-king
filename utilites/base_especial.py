from abc import ABC, abstractmethod
from enum import IntEnum

class Rank(IntEnum):
    COMUM = 1
    INCOMUM = 2
    RARO = 3
    EPICO = 4
    LENDARIO = 5
    UNICO = 6

class Especial(ABC):
    def __init__(self, nome, descricao, rank: Rank, efeito):
        self._nome = nome
        self._descricao = descricao
        self._rank = rank
        self._efeito = efeito

    @property
    def nome(self):
        return self._nome

    @property
    def descricao(self):
        return self._descricao

    @property
    def rank(self):
        return self._rank

    @property
    def efeito(self):
        return self._efeito


    