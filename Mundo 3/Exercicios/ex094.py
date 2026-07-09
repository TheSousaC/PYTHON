##Cadastrando Pessoas

bd = []
pessoas = {
    "nome": " ",
    "idade": 0,
    "sexo": " "
}
continuar = " "
media = 0

while True:
    pessoas["nome"] = str(input("Nome: "))
    pessoas["idade"] = int(input("Idade: "))
    pessoas["sexo"] = str(input("Sexo [M/F]: ")).upper().strip()[0]
    bd.append(pessoas.copy())
    pessoas.clear()
    continuar = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    if continuar == "N":
        break
for idade in bd:
    media += idade["idade"]

media = media / len(bd)
print("=" * 30)
print(f"- O grupo tem {len(bd)} pessoas")
print(f"- A média de idade do grupo é {media:.2f} anos")
print(f"- Lista das mulheres cadastradas são: ", end="")
for pessoa in bd:
    if pessoa["sexo"] == "F":
        print(f"{pessoa['nome']} ", end="")
print("-  Lista de pessoas que estão acima da média: ")
for pessoa in bd:
    if pessoa["idade"] > media:
        print(f"nome = {pessoa['nome']}; sexo = {pessoa["sexo"]}; idade = {pessoa["idade"]} ")
print("<<<ENCERRADO>>>")
