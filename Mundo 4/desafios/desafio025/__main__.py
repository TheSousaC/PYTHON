from transporte import *

def main():
    dist = 20

    entrega = Caminhão(dist)
    print(f"Frete de {type(entrega).__name__} em {dist}Km = {entrega.calcular_frete()}")

if __name__ == "__main__":
    main()