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
aluno = 0
print(f"N° Nome Media".center(30))
for c in range(0, len(info)):
    print(c ,info[c][0], end=" ")
    print(f"{info[c][3]:.2f}", end=" ")
    print()
while True:
    aluno = int(input("Digite o número do aluno para ver as notas dele [Digite 999 para parar]: "))
    print("=" * 30)
    print(f"As notas de {info[aluno][0]} são: {info[aluno][1]} e {info[aluno][2]}")
    if aluno == 999:
        break
