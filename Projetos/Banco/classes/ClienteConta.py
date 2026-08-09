from rich import print, inspect
from rich.panel import Panel


class Cliente:
    def __init__(self, nome: str, cpf: str, email: str):
        # Atributos de instância
        self._nome = None  # Protedigo (#)
        self._cpf = None  # Protedigo (#)
        self._email = None  # Protedigo (#)

        # Atributos Validados
        self.nome = nome
        self.cpf = cpf
        self.email = email

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor: str):
        self._nome = valor

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, valor: str):
        valor = valor.strip()
        if len(valor) != 11 or not valor.isdigit():
            raise ValueError("[red]CPF tem que ter 11 dígitos e somente números[/red]")
        else:
            self._cpf = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor: str):
        email = valor.strip()
        # Verifica se tem @ e divide a str entre no ponto do "@" e verifica de existem um "." no email
        if "@" not in email or "." not in email.split("@")[-1]:
            raise ValueError("[red]O Email inválido[/red]")
        else:
            self._email = email

    def exibir_dados(self):
        return f"Nome: {self.nome} \nCPF: {self.cpf} \nEmail: {self.email}\n"


class Conta:
    from datetime import datetime
    hoje = datetime.today().date()

    # Atributos de Instância
    def __init__(self, cliente: Cliente, numero: int, saldo: float = 0):
        self._cliente = cliente  # (#)
        self._numero = numero  # (#)
        self._saldo = saldo  # (#)
        self._extrato = []  # (#)

    @property
    def cliente(self):
        return self._cliente

    @property
    def numero(self):
        return self._numero

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O depósito deve ser maior que [red]R$0[/red]")
        else:
            self._saldo += valor
            self._extrato.append(f"Depósito de [green]+R${valor:.2f}[/] realizado em {Conta.hoje}.\n")
            print(f"Depósito de [green]+R${valor:.2f}[/] realizado em {Conta.hoje}")

    def sacar(self, valor: float):
        if valor <= 0:
            raise ValueError("[red]O valor do saque deve ser maior que R$0.00[/]")
        if valor > self.saldo:
            raise ValueError("[red]Saque insuficiente[/]")
        else:
            self._saldo -= valor
            self._extrato.append(f"\nSaque de [red]-R${valor:.2f}[/red] realizado em {Conta.hoje}.\n")
            print(f"Saque de [red]-R${valor:.2f}[/] realizado em {Conta.hoje}")

    def exibir_extrato(self):
        conteudo = ""
        for movimento in self._extrato:
            conteudo += f"{movimento}"
        if self._saldo <= 0:
            conteudo += f"\n[blue] Saldo atual: [red]{self._saldo}[/red][/blue]"
        else:
            conteudo += f"\n[blue] Saldo atual: [green]{self._saldo}[/green][/blue]"
        painel = Panel(conteudo, title=f"[blue]Extrato da conta: [green]{self._numero}[/green][blue]", width=60)
        print(painel)
