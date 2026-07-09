##DESAFIO, MEU XUXUUUUUU
## Nome e peso e printar o mais pesado e mais leve e todos os cadastrados

pessoas = []
dados = []
resposta = ""
pesado = leve = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: Kg')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])

    dados.clear() ##Isso salva vidas, limpa o array
    print("Pessoas cadastrada com sucesso!")
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print("=" * 30)
print(f"{len(pessoas)} pessoas foram cadastradas")
print(f"O maior peso foi de: {maior}. Peso de ", end="")
for p in pessoas:
    if p[1] == maior:
        print(f"{p[0]}", end="")
print()

print(f"O menor peso foi de: {menor}. Peso de ", end="")
for p in pessoas:
    if p[1] == menor:
        print(f"{p[0]}", end="")
