##Par e impar dnv xuxu

lista = []
listaPar = []
listaImpar = []
lista = listaPar, listaImpar

for c in range(0, 7):
    n = int(input("Digite um número bacana: "))
    if n % 2 == 0:
        listaPar.append(n)
    else:
        listaImpar.append(n)
    if c == 6:
        print("QUE NÚMERO TOP")
listaPar.sort()
listaImpar.sort()
print(f"Os números pares digitados foram: {listaPar}")
print(f"OS número impares digitados foram: {listaImpar}")
print("Só foram digitados número bacanas")