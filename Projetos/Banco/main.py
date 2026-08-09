from classes.ClienteConta import *
from classes.ContaCorrente import *


def main():
    # Cliente
    Cl01 = Cliente("Gabriel", "09876543210", "costasousagabriel@gmail.com")

    # ContaCorrente
    Cc = ContaCorrente(Cl01, 7008, 1_000, 500)
    Cc.sacar(1600)
    Cc.exibir_extrato()


if __name__ == "__main__":
    main()
