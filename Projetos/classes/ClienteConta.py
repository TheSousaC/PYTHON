from abc import ABC


class Cliente(ABC):
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

# class Conta(Cliente):
#     def __init__(self, nome:str, cpf:str, email:str, numero:int, saldo:float = 0, extrato:float):
#         super().__init__(nome, cpf, email)