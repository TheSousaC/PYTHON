##Média dos alunos

info = []
dados = []
resposta = " "

while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Nota 1: ")))
    dados.append(float(input("Nota 2: ")))
    media = (dados[1] + dados[2]) / 2
    dados.append(media)
    info.append(dados[:])
    dados.clear()
    resposta = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if resposta == "N":
        break
print("=" * 30)
print(f"N° Nome Media".center(30))
print("=" * 30)
