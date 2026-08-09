from classes.ClienteConta import *
from classes.ContaCorrente import *
from classes.ContaPoupanca import *


def main():
    # Cliente
    Cl01 = Cliente("Gabriel", "09876543210", "costasousagabriel@gmail.com")  # Cliente 1
    Cc = ContaCorrente(Cl01, 7008, 1_000, 500)  # Conta Corrente
    Cl02 = Cliente("Rafael", "12345678901", "Rafael123@gmail.com")  # Cliente 2
    Cp = ContaPoupanca(Cl02, 500, 100, 0.01)  # Conta Poupança

    try:
        # ContaCorrente
        Cc.sacar(1500)
        Cc.exibir_extrato()
    except Exception as e:
        print(f"Erro: {e}")

    try:
        # ContaPoupanca
        Cp.depositar(400)
        Cp.render_juros()
        Cp.sacar(505)
        Cp.exibir_extrato()
    except Exception as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    main()
