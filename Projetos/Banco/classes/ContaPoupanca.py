from classes.ClienteConta import Conta

class ContaPoupanca(Conta):
    def __init__(self, cliente, numero, saldo, taxa_juros = 0.005):
        super().__init__(cliente, numero, saldo)
        self._taxa_juros = taxa_juros


    @property
    def taxa_juros(self):
        return self._taxa_juros

    def render_juros(self):
        juros = self._saldo * self._taxa_juros
        self._saldo = self._saldo + juros
        self._extrato.append(f"Rendimetento de [green]+R${juros:.2f}.[/green]")
