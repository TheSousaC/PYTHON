from rich import print
from rich import inspect

class TheBank:
    """
    A classe TheBank cria uma conta bancaria que permite fazer saques e depositos
    """

    ##Atributos
    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"Conta {self.id} criada com sucesso na conta. Saldo atual: {self.saldo:,.2f}")

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem um saldo de R${self.saldo:,.2f}"

    ##Métodos
    def despositar(self, valor):
        self.saldo += valor
        print(f"Deposito de R${valor:,.2f} realizado com sucesso na conta de {self.titular}")

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saque de R${valor:,.2f} NEGADO!! Saldo insuficiente")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} realizado com sucesso na conta {self.titular}")


conta1 = TheBank(7405, "Gabriel Costa", 1000)