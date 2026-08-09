from rich import inspect

from classes.ClienteConta import Cliente
from classes.Banco import Bank
from classes.ContaCorrente import ContaCorrente


def main():
    #Banco
    TheBank = Bank("TheBank")
    # Cliente
    Cl01 = Cliente("Gabriel", "09876543210", "costasousagabriel@gmail.com")  # Cliente 1
    Cl02 = Cliente("Rafael", "12345678901", "Rafael123@gmail.com")  # Cliente 2

    conta_cc = TheBank.abrir_conta_corrente(Cl01,1000, 500)
    conta_cp = TheBank.abrir_conta_poupanca(Cl02,1000, 0.1)

    TheBank.listar_contas()
    TheBank.transferir(1001, 1002, 500)
if __name__ == "__main__":
    main()
