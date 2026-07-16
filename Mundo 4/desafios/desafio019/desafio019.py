##Classe Páginas
from time import sleep

from rich import print


class Livro:
    def __init__(self, titulo, paginas=1):
        self.titulo = titulo
        self.paginas = paginas
        self.pg_atual = 1
        print(
            f":book: [red]Você acabou de abrir o Livro: [blue]{self.titulo}[/] que tem [blue]{self.paginas} páginas[/]\nVocê agora está na página [blue]{self.pg_atual}[/][/]")

    def avancar_paginas(self, lidas):
        cont = 0
        for pg in range(0, lidas, 1):
            if not self.fim_do_livro():
                self.pg_atual += 1
                sleep(0.2)
                print(f"Página{self.pg_atual} :arrow_forward: ", end="")
                cont += 1
        print(f"\n[yellow]Você avançou {cont} e agora está na página[/] [green]{self.pg_atual}[/]")
        if self.fim_do_livro():
            print(f"Você chegou ao fim do livro [blue]{self.titulo}[/]")

    def fim_do_livro(self) -> bool:
        if self.pg_atual == self.paginas:
            return True
        else:
            return False


l1 = Livro(titulo="Livro 1", paginas=50)
l1.avancar_paginas(70)
