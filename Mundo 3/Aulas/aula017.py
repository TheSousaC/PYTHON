##ARRAY HAHAHAHHAHAAHAHHAHAHAAHHAAHHAHAHAHAHA

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista[2] = 150
lista.append(50)
# print(lista)

lista.insert(2, 1000)
# print(lista)
# lista.pop()
# lista.pop(10)
##lista.sort(reverse=True)
lista.remove(5)
lista.sort()
# print(lista)

# for indice, valor in enumerate(lista):
#     print(f"Na posição {indice}° {valor}!")

##Pra adicionar valores em uma lista em um for
listinha_show = []

for cont in range(0, 11):
    listinha_show.append(int(input("Digite um valor: ")))
print(listinha_show)