## Leitor infinito

maior = 0
menor = 0
numero = 0
media = 0
soma = 0
quantidade = 0

continuar = 'S'
while continuar == 'S':
    numero = int(input("Digite um numero inteiro: "))
    quantidade += 1
    continuar = str(input("Quer continuar? [S/N] ")).upper()
    soma += numero
    media = soma / quantidade
    if quantidade == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

if continuar != "N":
    print("Caracter não autenticado!")
else:
    print(
        f"A média entre todos os números digitados é {media}\nO maior numero digitado foi {maior}\nO menor numero digitado foi {menor}")