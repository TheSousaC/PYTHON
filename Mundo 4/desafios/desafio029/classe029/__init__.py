from rich import print, inspect

class Diario:
    def __init__(self, senha = "Girasol"):
        self.__senha = senha
        self.__segredos = []

    def escrever(self, segredinho):
        self.__segredos.append(segredinho)
        # print("[pruple]:shushing_face: Segredinho Guardado[/]")

    def ler(self, senha = None):
        if senha == None:
            print("Cadê a senha campeão?")
        else:
            if senha == self.__senha:
                print(f"[blue]Abrindo o Diário...[/]")
                for segredo in self.__segredos:
                    print(f":unlock: {segredo}")
            else:
                print("Senha incorreta!")