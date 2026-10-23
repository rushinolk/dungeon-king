from entidade.base import Personagem

class Player(Personagem):
    def __init__(self, nome, classe, level, vida, mana, forca, agilidade, inteligencia, sorte, percepcao, resistencia, XP_level,XP_levelAtual,atributos,dinheiro):
        super().__init__(nome, classe, level, vida, mana, forca, agilidade, inteligencia, sorte, percepcao, resistencia)
        self._XP_level = XP_level
        self._XP_levelAtual = XP_levelAtual
        self._atributos = atributos
        self._dinheiro = dinheiro
        