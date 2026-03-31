# Pegar os compimentos e caulcular a hipotenusa

from math import hypot

CatetoOposto = float(input('Digite o cateto oposto: '))
CatetoAdjacente = float(input('Digite o cateto adjacente: '))

Hipotenusa = hypot(CatetoOposto, CatetoAdjacente)

print(f"A hipotenusa de {CatetoAdjacente} e {CatetoAdjacente} é {Hipotenusa:.2f}")