from math import pi
from abc import ABC, abstractmethod
from rich import inspect


class Poligono(ABC):
    def __init__(self, lados):
        self.qnt_lados = lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, lado=1):
        super().__init__(4)
        self.lado = lado

    def area(self):
        area = self.lado ** 2
        return area

    def perimetro(self):
        perimetro = self.lado * 4
        return perimetro


class Circulo(Poligono):
    def __init__(self, raio=1):
        super().__init__(0)
        self.raio = raio

    def area(self):
        return pi * self.raio ** 2

    def perimetro(self):
        return 2 * pi * self.raio
