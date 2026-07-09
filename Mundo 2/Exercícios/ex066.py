## somador

num = soma = conatdor = 0

while True:
    num = int(input("Digite um número inteiro: "))
    if num == 999:
        break
    soma += num
    conatdor += 1
print(f"A soma dos valores digitados é de: {soma}\nA quantidade de valores digitados foi de: {conatdor}")