from classe029 import *

def main():
    D = Diario("Lula")
    D.escrever("Amo a Lua")
    D.escrever("Quero começar a escrever poesias, e ela é a minha inspiração")
    D.escrever("Segredinho")
    D.ler("Lula")

    # inspect(D, private=True, methods=True)

if __name__ == "__main__":
    main()