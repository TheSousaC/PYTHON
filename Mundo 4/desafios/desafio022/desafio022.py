from rich import print
from rich.panel import Panel


class ControleRemoto:
    canal_max: int = 10
    canal_min: int = 1
    volume_max: int = 10
    volume_min: int = 0

    def __init__(self, canal=1, volume=2):
        self.canal_atual: int = canal
        self.volume: int = volume
        self.ligado: bool = False

    def liga_desliga(self):
        self.ligado = not self.ligado

    def mostrarTV(self):
        conteudo = ""
        if not self.ligado:
            conteudo = f"[red]A Tv está desligada[/]"
        else:
            conteudo = f"CANAL  = "
            for canal in range(ControleRemoto.canal_min, ControleRemoto.canal_max + 1):
                if self.canal_atual == canal:
                    conteudo += f"[black on blue] {canal} [/]"
                else:
                    conteudo += f" {canal} "
            conteudo += f"\nVOLUME = "
            for volume in range(ControleRemoto.volume_min, ControleRemoto.volume_max + 1):
                if volume <= self.volume:
                    conteudo += f"[black on cyan] [/]"
                else:
                    conteudo += f"[black on white] [/]"
        TV = Panel(conteudo, title="[ TV ]", width=45)
        print(TV)

    def canal_mais(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_max:
                self.canal_atual = ControleRemoto.canal_min
            else:
                self.canal_atual += 1

    def canal_menos(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_min:
                self.canal_atual = ControleRemoto.canal_max
            else:
                self.canal_atual -= 1

    def volume_mais(self):
        if self.ligado:
            if self.volume != ControleRemoto.volume_max:
                self.volume += 1

    def volume_menos(self):
        if self.ligado:
            if self.volume != ControleRemoto.volume_min:
                self.volume -= 1


tv = ControleRemoto()
while True:
    tv.mostrarTV()
    comando = str(input("< CH >  - VOL + "))
    match comando:
        case "0":
            break
        case "@":
            tv.liga_desliga()
        case "<":
            tv.canal_menos()
        case ">":
            tv.canal_mais()
        case "-":
            tv.volume_menos()
        case "+":
            tv.volume_mais()
    print("\n" * 10)
