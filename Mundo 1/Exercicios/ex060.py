## Fatorial

from math import factorial

numero = int(input("Digite um numero entre 0 e 10: "))
c = numero
f = factorial(numero)
while c > 0:
    print(f"{c}", end="")
    print(" x " if c > 1 else " = ", end="")
    c -= 1