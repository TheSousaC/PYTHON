# ler um numero real e mostrar ele em int

from math import trunc

Numero = float(input("Digite um numero quebrado: "))

NumeroInt = trunc(Numero)

print(f"{Numero} transformado em inteiro é {NumeroInt}")