## array?
somaidade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeHomemMaisVelho = ''
totMulher20 = 0
for p in range(1, 5):
    print(f"------ {p}° PESSOA ------")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaidade += idade
    if p == 1 and sexo in "Mm":
        maiorIdadeHomem = idade
        nomeHomemMaisVelho = nome
    if sexo in "Mm" and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeHomemMaisVelho = nome
    if sexo in "Ff" and idade < 20:
        totMulher20 += 1
mediaIdade += somaidade / 4
print(f"A média da idade do grupo é de: {mediaIdade} anos")
print(f"O homem mais vellho tem {maiorIdadeHomem} anos e se chama {nomeHomemMaisVelho}")
print(f"Ao todo são {totMulher20} mulheres com menos de 20 anos")