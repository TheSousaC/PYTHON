class Cliente():
    def __init__(self, nome: str, cpf: str, email: str):
        #Atributos de instância
        self._nome = None #Protedigo (#)
        self._cpf = None #Protedigo (#)
        self._email = None #Protedigo (#)

        #Atributos Validados
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
            raise ValueError("CPF tem que ter 11 dígitos e somente números")
        else:
            self._cpf = valor


    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor: str):
        email = valor.strip()
        #Verifica se tem @ e divide a str entre no ponto do "@" e verifica de existem um "." no email
        if "@" not in email or "." not in email.split("@")[-1]:
            raise ValueError("O Email inválido")
        else:
            self._email = email

    def exibir_dados(self):
        return f"Nome: {self.nome} \nCPF: {self.cpf} \nEmail: {self.email}\n"

class Conta():
    #Atributos de Instância
    def __init__(self, cliente: Cliente, numero:int, saldo:float = 0):
        self._cliente = cliente # (#)
        self._numero = numero # (#)
        self._saldo = saldo # (#)
        self._extrato = [] # (#)

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, valor):
        raise PermissionError("Você não pode mudar o cliente!")

    @property
    def numero(self):
        return self._numero
    @numero.setter
    def numero(self, valor):
        raise PermissionError("Não é possivel mudar o número da conta")

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        raise PermissionError("Não é possivel mudar o saldo. Altere através de depósitos ou saques")

