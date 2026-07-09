##Função de gerar números e de somar os pares

from random import randint


def sorteio():
    num = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
    return num


def somaPar(num):
    s = 0
    for c in num:
        if c % 2 == 0:
            s += c
    return s


##Principal
numeros = sorteio()
print(f"Sorteando os valores da lista: {numeros}. PRONTO!")
somaPares = somaPar(numeros)
print(f"A soma dos números pares de {numeros} é: {somaPares}")
