from dbm import error

from rich import print, inspect


class Termostato:
    def __init__(self, temperatura=20):
        self.__temperatura = temperatura

    @property
    def temperatura(self): # Getter (Aparece)
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor): # Setter (Muda o Valor)
        if valor > 30 or valor < 16:
            if valor > 30:
                self.__temperatura = 30
            if valor < 16:
                self.__temperatura = 16
        else:
            if valor % 1 == 0 or valor % 0.5 == 0:
                self.__temperatura = valor
            else:
                raise ValueError(f"A temperatura de {valor} é invalida")

    @property
    def ftemperatura(self):
        return f"{self.__temperatura}°C"