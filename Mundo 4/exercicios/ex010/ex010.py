from rich import print, inspect


class Avaliacao:
    def __init__(self, nome, diciplina, nota=0):
        self.nome = nome
        self.diciplina = diciplina
        self._nota = nota

    # Criando Atributo Validável
    @property
    def nota(self): # Seria o Getter
        return self._nota

    @nota.setter
    def nota(self, valor): # Seria o Setter
        if valor >= 0 and valor <= 10:
            self._nota = valor
        else:
            print("Valor invalido!")
