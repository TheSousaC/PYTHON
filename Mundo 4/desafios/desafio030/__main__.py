from classe030 import *

def main():
    crecre = Credencial()
    crecre.senha = "Luar"
    crecre.validar("Luar")
    inspect(crecre, methods=True, private=True)

if __name__ == "__main__":
    main()