##Add valores menos valores repetidos

lista =  []
continuar = 'S'
while True:
    lista.append(int(input("Digite um valor: ")))
    # n = int(input("Difite"))
    # lista.append(n)
    continuar = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
    while continuar != 'S' and continuar != 'N':
        continuar = str(input("Resposta não verificada, digite novamente uma das duas opções [S/N]: ")).strip().upper()[0]
    if continuar == 'N':
        break
print(lista)