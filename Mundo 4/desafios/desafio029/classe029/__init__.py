from rich import print, inspect

class Diario:
    def __init__(self, senha = "Girasol"):
        self.__senha = senha.strip()
        self.__segredos = []

    @property
    def senha(self):
        raise PermissionError("Ninguem tem permissão de ler o diário")

    @senha.setter
    def senha(self, novasenha):
        self.__senha = novasenha.strip()

    def escrever(self, segredinho):
        self.__segredos.append(segredinho.strip())
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
                raise PermissionError("Senha invalida!")