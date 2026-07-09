## Somador ou sla oq
numero = 0
soma = 0
quantidade = 0
while numero != 999:
    numero = int(input("Digite Um número de 0 até 999: "))
    if numero == 999:
        print(f"A soma dos números foi de: {soma} e quantidade foi de: {quantidade}")
    else:
        soma += numero
        quantidade += 1
print("Fim")