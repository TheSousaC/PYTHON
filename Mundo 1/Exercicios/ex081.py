numeros = []
num = 0
cont = 0
continuar = ''
while True:
    num = int(input("Digite um número serelepe: "))
    numeros.append(num)
    cont += 1
    continuar = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    if continuar == 'N':
        break
numeros.sort(reverse=True)
print(f"Você digitou {numeros[cont]} numeros")
print(f"Os numeros digitados foram {numeros}")
if 5 in numeros:
    print("O valor 5 está no array")