from rich import print, inspect

class Retangulo:
    def __init__(self, base = None, altura = None):
        self._base = base
        self._altura = altura
        self._area = base * altura

    @property
    def base(self):
        return self._base

    @property
    def altura(self):
        return self._altura

    @property
    def area(self):
        return self._area

    @base.setter
    def base(self, base):
        self._base = base
        self._area = self._altura * self._base

    @altura.setter
    def altura(self, altura):
        self._altura = altura
        self._area = self._altura * self._base

    @property
    def medidas(self):
        return (f"As medidas usadas foram: Altura: {self._altura} & Base: {self._base} = Área: {self._area}")