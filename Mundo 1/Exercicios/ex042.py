## Triangulo v2

r1 = float(input("Digite o primeiro segmento: "))
r2 = float(input("Digite o segundo segmento: "))
r3 = float(input("Digite o terceiro segmento: "))
if r1 < r2 + r3 and r2 < r3 + r3:
    print("Esses segmentos podem se tornar um triangulo")
    if r1 == r2 and r3 == r1:
        print("O triangulo é Equilátero.")
    elif r1 == r2 and r3 != r1:
        print("O triangulo é Isósceles.")
    else:
        print("O triangulo é Escaleno")
else:
    print("Esses segmentos nao formam um triangulo")
