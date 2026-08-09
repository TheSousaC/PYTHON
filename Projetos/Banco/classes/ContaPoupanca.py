from classes.ClienteConta import Conta

class ContaPoupanca(Conta):
    def __init__(self, cliente, numero, saldo, taxa_juros = 0.005):
        super().__init__(cliente, numero, saldo)
        self._juros_juros = taxa_juros
