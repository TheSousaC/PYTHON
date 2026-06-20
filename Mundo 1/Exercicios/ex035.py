## Ver retas para fazer um triangulo

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r3 + r1 and r3 <r1 + r2:
    print("Os segmentos podem ser tornar um triangulo")
else:
    print("Os segmentos nao podem ser um triangulo")