from abc import ABC, abstractmethod
from rich import inspect

class Transporte(ABC):
    def distancia(self):
        pass

    def frete(self):
        frete = self.calcular_frete()
        return frete

    @abstractmethod
    def calcular_frete(self):
        pass


class Moto(Transporte):

    fator = 0.5

    def __init__(self, distancia):
        self.distancia = distancia

    def calcular_frete(self):
        frete = self.distancia * self.fator
        frete = round(frete, 2)
        return frete


class Drone(Transporte):

    fator = 9.50

    def __init__(self, distancia):
        self.distancia = distancia

    def calcular_frete(self):
        if self.distancia < 10:
            frete = self.distancia * self.fator
            frete = round(frete, 2)
            return frete
        else:
            return f"A distância passa de 10km, não há como fazer a entrega por drone"


class Caminhão(Transporte):

    fator = 1.20

    def __init__(self, distancia):
        self.distancia = distancia

    def calcular_frete(self):
        if self.distancia < 50:
            return f"Não é possivel fazer uma entrega por caminhão em uma distância menor de 50km"
        else:
            frete = self.distancia * self.fator
            frete = round(frete, 2)
            return frete
