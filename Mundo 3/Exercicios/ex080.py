##Sem usar o sorted

numeros = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > numeros[-1]:
        numeros.append(n)
    else:
        posicao = 0
        while posicao < len(numeros):
            if n <= numeros[posicao]:
                numeros.insert(posicao, n)
                posicao += 1
                break
print(f"Os valores em ordem foram {numeros}")