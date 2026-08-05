from classe032 import *

def main():
    conta = TheBank("7", "Gabriel", 1_000, "Luar")
    conta.nome = "Dani"
    conta.sacar(500)
    conta.depositar(5_000_000)
    # inspect(conta, private=True, methods=True)
if __name__ == "__main__":
    main()