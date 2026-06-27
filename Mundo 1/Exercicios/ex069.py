## cadastro de informações

idade = 0
sexo = ""
velhos = 0
homens = 0
pergunta = ""
mulheres20 = 0
contador = 1

while True:
    idade = int(input(f"Digite a idade da {contador} pessoa: "))
    sexo = str(input(f"Digite o sexo da {contador} pessoa [F/M]: ")).strip().upper()[0]
    contador += 1
    pergunta = str(input(f"Quer continuar? [S/N] ")).strip().upper()[0]
    if pergunta != "S" and pergunta != "N":
        pergunta = str(input(f"Quer continuar? [S/N] ")).strip().upper()[0]
    if idade >= 18:
        velhos += 1
    if  sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulheres20 += 1
    if pergunta == "N":
        break

if idade >= 18:
    print(f"Temos {velhos} pessoas maiores de 18 cadastrados.")
if homens == 1:
    print(f"Temos apenas {homens} homem cadastrado.")
else:
    print(f"Temos {homens} homens cadastrados.")
if mulheres20 == 0:
    print(f"Não temos nenhuma mulher menor de 20 anos de idade cadastrados.")
elif mulheres20 == 1:
    print(f"Temos apenas {mulheres20} mulher cadastrada menor de 20 anos")
else:
    print(f"Temos {mulheres20} mulher menores de 20 anos.")
