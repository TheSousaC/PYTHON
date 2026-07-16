##Classe Caneta
from rich import print
class Caneta:
    def __init__(self, cor="azul"):
        escolha = ""
        match cor.lower().strip():
            case "azul":
                escolha = "[blue]"
            case "vermelho" | "vermelha":
                escolha = "[red]"
            case "verde":
                escolha = "[green]"
            case _:
                escolha = "[white]"
        self.cor = escolha
        self.tamapada = True

    def escrever(self, msg):
        if self.tamapada:
            print(f"A {self.cor}caneta[/] está tapada")
        else:
            print(f"{self.cor}{msg}[/]", end=" ")

    def tampar(self):
        self.tamapada = True

    def destampar(self):
        self.tamapada = False

    def quebrar_linha(self, qnt = 1):
        print("\n" * qnt, end="")


c1 = Caneta("vermelha")
c2 = Caneta("Azul")
c1.destampar()
c2.destampar()
c1.escrever("OIOIOI")
c1.quebrar_linha(2)
c2.escrever("Funciona?")
