from classes.ClienteConta import *

def main():
    Cl01 = Cliente("Gabriel", "09876543210", "costasousagabriel@gmail.com")
    Cnt01 = Conta(Cl01, 7008, 1_000)
    Cnt01.despositar(500)
    Cnt01.exibir_extratos()
if __name__ == "__main__":
    main()