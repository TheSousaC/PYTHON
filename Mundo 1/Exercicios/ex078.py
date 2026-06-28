##Ver maior e menor e em  qual posição estão
lista = []
print("Digite 5 valores abaixo:")
for c in range(0, 6):
    lista.append(int(input(f"Digite o {c} valor: ")))
print(lista)
print(f"O menor valor é {min(lista)} e está na posição {lista.index(min(lista))}")
print(f"O maior valor é {max(lista)} e está na posição {lista.index(max(lista))}")