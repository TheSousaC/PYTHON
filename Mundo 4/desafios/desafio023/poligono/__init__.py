from math import pi
from abc import ABC, abstractmethod
from rich import inspect


class Poligono(ABC):
    def __init__(self, qnt_lados=1):
        self.qnt_lados = qnt_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, lado, qnt_lados = 4):
        super().__init__(qnt_lados)
        self.lado = lado

    def area(self):
        area = self.lado * self.lado
        return area

    def perimetro(self):
        perimetro = self.lado * self.qnt_lados
        return perimetro


class Circulo(Poligono):
    def __init__(self, raio, qnt_lados = 1):
        super().__init__(qnt_lados)
        self.raio = raio

    def area(self):
        return pi * self.raio ** 2

    def perimetro(self):
        return 2 * pi * self.raio
