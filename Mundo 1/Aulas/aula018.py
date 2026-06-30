# teste = []
# teste.append("Gabriel")
# teste.append(18)
# galera = []
# galera.append(teste[:])
# teste[0] = "BIBI"
# teste[1] = 19
# galera.append(teste[:])
# print(galera)
#

# galera = [
#     ["Gabriel", 18],
#     ["Rafael", 12],
#     ["Aleatorio", 00]
# ]

# print(galera[2][1])

# for p in galera:
#     print(p[0])

dados = []
pessoas = []

for c in range(0, 3):
    dados.append(str(input("Digite uma nome: ")))
    dados.append(int(input("Digite uma idade: ")))
    pessoas.append(dados[:])
    dados.clear()
print(pessoas)