from rich import print, inspect
from poligono import *

def main():
    p1 = Quadrado(20)
    print(f"Um Quadrado de lado {p1.lado} tem perimetro de {p1.perimetro()}mm")
    print(f"Um Quadrado de lado {p1.lado} tem a área de {p1.area()}mm²")

    p2 = Circulo(12)
    print(f"Um Circulo de raio {p2.raio} tem o perimetro de {p2.perimetro():.1f}mm")
    print(f"Um Circulo de raio {p2.raio} tem a área de {p2.area():.1f}mm²")

if __name__ == "__main__":
    main()