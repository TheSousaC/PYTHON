from classes.ClienteConta import *
from rich import print, inspect

def main():
    Cliente01 = Cliente("Gabriel", "09876543210", "costasousagabriel@gmail.com")
    Conta01 = Conta(Cliente01, 7008, 1_000)
    inspect(Conta01, private=True)
if __name__ == "__main__":
    main()