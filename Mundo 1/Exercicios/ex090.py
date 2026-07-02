##Nome e média

aluno = {
    "nome": "",
    "media": ""
}

aluno["nome"] = str(input("Digite o nome do aluno: "))
aluno["media"] = float(input("Digite a média: "))

if aluno["media"] >= 5:
    aluno["situacao"] = "Aprovado"
else:
    aluno["situacao"] = "Reprovado"
print(f"O aluno {aluno['nome']} foi aprovado!")
