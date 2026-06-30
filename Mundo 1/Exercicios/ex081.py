numeros = []
num = 0
continuar = ''
while True:
    num = int(input("Digite um número serelepe: "))
    numeros.append(num)
    continuar = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    if continuar == 'N':
        break
numeros.sort(reverse=True)
print(f"Você digitou {len(numeros)} numeros")
print(f"Os numeros digitados foram {numeros}")
if 5 in numeros:
    print("O valor 5 está no array")
else:
    print("O valor 5 não foi encontrado")