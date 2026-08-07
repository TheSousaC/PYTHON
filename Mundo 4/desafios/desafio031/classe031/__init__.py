from rich import print, inspect


class Retangulo:
    def __init__(self, base=1, altura=1):
        self._base = None
        self._altura = None
        self._area = None

        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self._base

    @property
    def altura(self):
        return self._altura

    @property
    def area(self):
        self._area = self.altura * self.base
        return self._area

    @base.setter
    def base(self, base):
        if not isinstance(base, int) and not isinstance(base, float):
            raise TypeError("O valor da base deve ser um número")
        if base < 0:
            raise ValueError("O valor da base deve ser maior que 0")
        else:
            self._base = base

    @altura.setter
    def altura(self, altura):
        if not isinstance(altura, int) and not isinstance(altura, float):
            raise TypeError("O valor da altura deve ser um número")
        if altura < 0:
            raise ValueError("O valor da altura deve ser maior que 0")
        else:
            self._altura = altura

    @property
    def medidas(self):
        return (f"As medidas usadas foram: Altura: {self._altura} & Base: {self._base}")

    @medidas.setter
    def medidas(self, valores:tuple):
        if len(valores) != 2:
            raise SyntaxError("Tem que ser passados dois valores")
        if isinstance(valores[0], float) or isinstance(valores[1], int):
            self._base = valores[0]
        else:
            raise TypeError("A base tem que ser um número")
        if isinstance(valores[1], float) or isinstance(valores[1], int):
            self._altura = valores[1]
        else:
            raise TypeError("A altura tem que ser um número")

    @area.setter
    def area(self, altura):
        raise PermissionError("Você não pode definia a área desta maneira")
