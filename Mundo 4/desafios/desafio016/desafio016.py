##Funcionario
from rich import print
from rich import inspect

class Funcionario:
    ##Atributos de Classe
    empresa = "Bacana Soluções"

    ##Atributos de Instância
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    ##Metodos
    def apresentação(self) -> str:
        return f"Olá :smile:, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da {Funcionario.empresa}"


f1 = Funcionario("Fernando", "TI", "Designer")
# inspect(f1, methods=True)
print(f1.apresentação())
f2 = Funcionario("Kamille", "Rh", "Entrevistadora")
#inspect(f2)
print(f2.apresentação())
