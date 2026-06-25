## Fatorial

from math import factorial

numero = int(input("Digite um número pra fatorar: "))
fatorial = 1

while numero > 0:
    fatorial *= numero
    numero -= 1
print(fatorial) 