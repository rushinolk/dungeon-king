from abc import ABC, abstractmethod


class Personagem(ABC):
    def __init__(self, nome, classe,level, vida, mana, forca, agilidade, inteligencia,sorte,percepcao,resistencia):
        self._nome = nome
        self._classe = classe
        self._level = level
        self._vida = vida
        self._mana = mana
        self._forca = forca
        self._agilidade = agilidade
        self._inteligencia = inteligencia
        self._sorte = sorte
        self._percepcao = percepcao
        self._resistencia = resistencia

    @property
    def nome(self):
        return self._nome

    @property
    def classe(self):
        return self._classe

    @property
    def level(self):
        return self._level

    @property
    def vida(self):
        return self._vida

    @property
    def mana(self):
        return self._mana

    @property
    def forca(self):
        return self._forca

    @property
    def agilidade(self):
        return self._agilidade

    @property
    def inteligencia(self):
        return self._inteligencia

    @property
    def sorte(self):
        return self._sorte

    @property
    def percepcao(self):
        return self._percepcao

    @property
    def resistencia(self):
        return self._resistencia

    @nome.setter
    def nome(self, value):
        self._nome = value

    @classe.setter
    def classe(self, value):
        self._classe = value

    @level.setter
    def level(self, value):
        if value < 1:
            raise ValueError("O nível deve ser maior ou igual a 1.")
        self._level = value

    @vida.setter
    def vida(self, value):
        if value < 0:
            self._vida = 0
        self._vida = value

    @mana.setter
    def mana(self, value):
        if value < 0:
            self._mana = 0
        self._mana = value

    @forca.setter
    def forca(self, value):
        if value < 0:
            raise ValueError("A força não pode ser negativa.")      
        self._forca = value

    @agilidade.setter
    def agilidade(self, value):
        if value < 0:
            raise ValueError("A agilidade não pode ser negativa.")
        self._agilidade = value

    @inteligencia.setter
    def inteligencia(self, value):
        if value < 0:
            raise ValueError("A inteligência não pode ser negativa.")
        self._inteligencia = value

    @sorte.setter
    def sorte(self, value):
        if value < 0:
            raise ValueError("A sorte não pode ser negativa.")
        self._sorte = value

    @percepcao.setter
    def percepcao(self, value):
        if value < 0:
            raise ValueError("A percepção não pode ser negativa.")
        self._percepcao = value

    @resistencia.setter
    def resistencia(self, value):
        if value < 0:
            raise ValueError("A resistência não pode ser negativa.")
        self._resistencia = value


    @abstractmethod
    def atacar(self, alvo):
        pass

    @abstractmethod
    def receber_dano(self, dano):
        pass


