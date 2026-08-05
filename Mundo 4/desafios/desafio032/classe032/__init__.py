import hashlib
from rich import print, inspect


class TheBank:
    def __init__(self, id, nome, saldo, chave=None):
        self._id = id
        self._titular = nome
        self.__saldo = saldo
        self.__hash = chave

        if self.__hash is None:
            senha = self.pede_senha()
            self.__hash = hashlib.sha256(str(senha).encode()).hexdigest()
            print(f"[green]Conta de {self._titular} criada com sucesso! Saldo disponivel: [cyan]R${self.__saldo:.2f}[/cyan][/green]")
        else:
            self.__hash = hashlib.sha256(str(chave).encode()).hexdigest()
            print(f"[green]Conta de {self._titular} criada com sucesso! Saldo disponivel: [cyan]R${self.__saldo:.2f}[/cyan][/green]")



    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self, nome):
        senha = self.pede_senha()
        senha = self.validar_senha(senha)

        if senha:
            self._titular = nome
            print(f"[green]O nome do titular da conta {self._id} mudou para [cyan]{self._titular}[cyan][/green]")
        else:
            print("Senha invalida!")


    def pede_senha(self) -> str:
        senha = input("Senha: ")
        return senha


    def validar_senha(self, senha) -> bool:
        senha_hash = hashlib.sha256(str(senha).encode()).hexdigest()
        if senha_hash == self.__hash:
            return True
        else:
            return False

    def sacar(self,valor, senha = None):
        if senha == None:
            senha = self.pede_senha()
            senha = self.validar_senha(senha)
            if senha:
                valor = abs(valor)
                self.__saldo -= valor
                print(f"[green]Foi realizado um saque de [red]R${valor:.2f}[/red] na conta de [cyan]{self._titular}[/cyan][/green]")
            else:
                print("Senha invalida!\nSaque invalido")
        else:
            senha = self.validar_senha(senha)
            if senha:
                valor = abs(valor)
                self.__saldo -= valor
                print(f"[green]Foi realizado um saque de [red]R${valor:.2f}[/red] na conta de [cyan]{self._titular}[/cyan][/green]")
            else:
                print("Senha invalida!\nSaque invalido")


    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f"[green]OPA, foi depositado um valor de [purple]R${valor:,.2f}[/purple] na conta de [cyan]{self._titular}[/cyan][/green]")