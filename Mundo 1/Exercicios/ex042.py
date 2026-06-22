## Triangulo v2

r1 = float(input("Digite o primeiro segmento: "))
r2 = float(input("Digite o segundo segmento: "))
r3 = float(input("Digite o terceiro segmento: "))

if r1 == r2 and r3 == r1:
    print("Os segmentos podem ser iguais. O triangulo é Equilátero.")
elif r1 == r2 and r3 != r1:
    print("Dois lados iguais. O triangulo é Isósceles.")
else:
    print("Todos os lados são diferentes. O triangulo é Escaleno")