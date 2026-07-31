import random
from abc import ABC, abstractmethod
from rich import print, inspect


class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo, forca=30):
        if self.vida > 0 and alvo.vida > 0:
            # Pode dar o golpe
            golpe = self.golpes[random.randrange(0, len(self.golpes))]

            print(
                f"[blue]{self.nome}[/]({self.vida}) atacou [purple]{alvo.nome}[/]({alvo.vida}) com um [red]{golpe}[/] de força {forca}")
            alvo.receber_dano(forca)
        else:
            print(f"O Ataque de {self.nome} -> {alvo.nome} não pode acontecer!")

    def receber_dano(self, dano):
        fator = random.randint(0, dano)
        self.vida -= fator
        if self.vida < 0:
            self.vida = 0
        print(f"[purple]{self.nome}[/] recebeu [red]{fator}[/] de [red]dano[/]")

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Soco Potente", "Golpe de Machado", "Golpe Aéreo"]

    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        print(f"[blue]{self.nome}[/] usou uma atadura e recuperou [green]{fator}[/] pontos de [green]vida[/]")


class Mago(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Bola de Fogo", "Trovões", "Indefinido"]

    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        print(f"[blue]{self.nome}[/] bebeu uma poção e recuperou [green]{fator}[/] pontos de [green]vida[/]")
