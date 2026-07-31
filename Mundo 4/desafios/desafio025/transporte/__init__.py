from abc import ABC, abstractmethod
from rich import inspect


class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        self. frete = 0

    @abstractmethod
    def calcular_frete(self):
        pass


class Moto(Transporte):
    fator = 0.50

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        self.frete = self.distancia * Moto.fator
        return f"R${self.frete:.2f}"



class Drone(Transporte):
    fator = 9.50

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        if self.distancia < 10:
            self.frete = self.distancia * Drone.fator
            return f"{self.frete:.2f}"
        else:
            return f"A distância passa de 10km, não há como fazer a entrega por drone"


class Caminhão(Transporte):
    fator = 1.20

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        if self.distancia < 50:
            return f"O Raio minimo é de 50Km"
        else:
            self.frete = self.distancia * Caminhão.fator
            return f"R${self.frete:.2f}"
