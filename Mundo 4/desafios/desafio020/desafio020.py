from rich import print
from rich.panel import Panel
from rich import inspect

class Gamer:

    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favorito = []

    def add_favorito(self, game):
        self.favorito.append(game)
        self.favorito = sorted(self.favorito, key=str.lower)

    def ficha(self):
        conteudo = f"Nome real: [blue]{self.nome}[/]"
        conteudo += f"\nJogos Favoritos:"
        for num, game in enumerate(self.favorito):
            conteudo += f"\n:poop: {game}"
        painel = Panel(conteudo, title=self.nick, width=40)
        print(painel)

j1 = Gamer(nome="Gabriel", nick="<Seu Pai>")
j1.add_favorito("Crash")
j1.add_favorito("MineCraft")
j1.add_favorito("Roblox")
j1.add_favorito("Among Us")
j1.add_favorito("Subnautica")
j1.add_favorito("Fars To Phantom")
j1.ficha()