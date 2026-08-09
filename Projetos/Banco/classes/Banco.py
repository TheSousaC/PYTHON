from classes.ContaCorrente import ContaCorrente
from classes.ContaPoupanca import ContaPoupanca
from classes.ClienteConta import *
from rich import print
from rich.panel import Panel


class Bank:
    def __init__(self, nome: str):
        self._nome = nome
        self._contas = []

    @property
    def nome(self):
        return self._nome

    @property
    def contas(self):
        return self._contas

    def abrir_conta_corrente(self, cliente, saldo: float = 0, limite_cheque_especial=500):
        numero = len(self._contas) + 1001  # Vai criar um número de acordo com a quantidades de contas existentes
        nova_conta = ContaCorrente(cliente, numero, saldo, limite_cheque_especial)
        self._contas.append(nova_conta)
        print(f"Conta Corrente N°{numero} criada para {cliente.nome}")

    def abrir_conta_poupanca(self, cliente, saldo: float = 0, taxa_rendimento=0.001):
        numero = len(self._contas) + 1001
        nova_conta = ContaPoupanca(cliente, numero, saldo, taxa_rendimento)
        self._contas.append(nova_conta)
        print(f"Conta Corrente N°{numero} criada para {cliente.nome}")

    def buscar_conta(self, numero):
        for conta in self._contas:
            if numero == conta.numero:
                return conta
        return None

    def transferir(self, numero_origem: int, numero_destino: int, valor: float):
        origem = self.buscar_conta(numero_origem)
        destino = self.buscar_conta(numero_destino)

        if origem is None or destino is None:
            raise ValueError("[red]Conta de origem ou destinataria não existe[/red]")

        origem.sacar(valor)
        destino.sacar(valor)
        print(f"Transferencia de R${valor} feita de {numero_origem} para {numero_destino}")

    def listar_contas(self):
        conteudo = ""
        for conta in self._contas:
            tipo = type(conta).__name__
            conteudo += f"N°{conta.numero} | Tipo: {tipo}| Titular: {conta.cliente.nome} | Saldo: R${conta.saldo:.2f}\n"
        painel = Panel(conteudo, title=f"Contas de {self._nome}", width=90)
        print(painel)
