##Listar par e lista impar

lista = []
listaPar = []
listaImpar = []

num = 0
continuar = ""

while True:
    lista.append(int(input("Digite um numero: ")))
    continuar = str(input("Deseja continuar? [S/N]")).upper().strip()[0]
    if continuar == "N":
        break

for cont in range(0, len(lista)):
    if lista[cont] % 2 == 0:
        listaPar.append(lista[cont])
    else:
        listaImpar.append(lista[cont])

print(lista)
print(listaPar)
print(listaImpar)