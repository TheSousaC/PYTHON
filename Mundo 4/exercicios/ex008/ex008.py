##Conta Bancaria

class TheBank:
    """
    A classe TheBank cria uma conta bancaria que permite fazer saques e depositos
    """

    ##Atributos
    def __init__(self, id, nome, saldo=0):
        self.id = id # Público (+)
        self._titular = nome # Protegido (#)
        self.__saldo = saldo # Privado (-)
        print(f"Conta {self.id} criada com sucesso na conta. Saldo atual: {self.__saldo:,.2f}")

    def __str__(self):
        return f"A conta {self.id} de {self._titular} tem um saldo de R${self.__saldo:,.2f}"

    ##Métodos
    def despositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f"Deposito de R${valor:,.2f} realizado com sucesso na conta de {self._titular}")

    def sacar(self, valor):
        valor = abs(valor)
        if valor > self.__saldo:
            print(f"Saque de R${valor:,.2f} NEGADO!! Saldo insuficiente")
        else:
            self.__saldo -= valor
            print(f"Saque de R${valor:,.2f} realizado com sucesso na conta {self._titular}")

