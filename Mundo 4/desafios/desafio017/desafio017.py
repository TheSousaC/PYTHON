##Classe Produto
from rich import print, box
from rich.panel import Panel
from rich.traceback import install
install()

class Produto:
    def __init__(self, nome, preco):
        ##Atributos
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        conteudo = f"{self.nome.center(30, ' ')}"
        conteudo += f"{'-' * 30}"
        precoF = f"R$ {self.preco:,.2f}"
        conteudo += f"{precoF.center(30, ' ')}"
        etiqueta = Panel( conteudo, title="Produto", width=34)
        print(etiqueta)


p = Produto("Iphone 17 pro max", 6_000.99)
p.etiqueta()
p2 = Produto("Café", 49)
p2.etiqueta()