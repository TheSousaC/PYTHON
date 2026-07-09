##Add valores menos valores repetidos

lista =  []
continuar = 'S'
while True:
    n = int(input("Digite um número: "))
    while True:
        if n not in lista:
            lista.append(n)
            break
        else:
            print("Epa pera lá")
            n = int(input("Esse número já foi digitado. Por Favor, digite outro: "))
            if n not in lista:
                lista.append(n)
                break
    continuar = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
    while continuar != 'S' and continuar != 'N':
        continuar = str(input("Resposta não verificada, digite novamente uma das duas opções [S/N]: ")).strip().upper()[0]
    if continuar == 'N':
        break
lista.sort()
print(lista)