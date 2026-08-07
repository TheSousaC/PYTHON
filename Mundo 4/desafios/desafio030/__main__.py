from classe030 import *

def main():
    crecre = Credencial()
    crecre.senha = "MissPurple"
    print(crecre.senha)
    crecre.validar("MissPurple")
    inspect(crecre, methods=True, private=True)

if __name__ == "__main__":
    main()