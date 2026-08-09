from classes.ClienteConta import Conta
from rich import print


class ContaCorrente(Conta):
    def __init__(self, cliente, numero, saldo=0, limite_cheque_especial=None):
        super().__init__(cliente, numero, saldo)
        self.limite_cheque_especial = limite_cheque_especial

    @property
    def limite_cheque_especial(self):
        return self._limite_cheque_especial

    @limite_cheque_especial.setter
    def limite_cheque_especial(self, valor):
        valor = abs(valor)
        self._limite_cheque_especial = valor

    def sacar(self, valor):
        from datetime import datetime
        hoje = datetime.today().date()
        if valor <= 0:
            raise ValueError("O valor do saque deve ser maior que 0")
        if valor > self._saldo + self.limite_cheque_especial:
            raise PermissionError("Saldo Insuficiente")
        else:
            self._saldo -= valor
            self._extrato.append(f"Saque de [red]-R${valor:.2f}[/] realizado em {hoje}\n")
            print(f"[green]Saque realizado com sucesso[/green]")
