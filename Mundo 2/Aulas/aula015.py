## Breack
soma = 0
contador = 0
while True:
    numero = int(input("Digite um número: "))
    soma += numero
    contador += 1
    if numero == 999:
        break
print(f"{soma} foi a soma")
print("FIM")