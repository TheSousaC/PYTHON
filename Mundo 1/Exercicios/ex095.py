## Aprimoramento do Ex093

jogadores = []
continuar = ""

while True:
    informacao = {
        "nome": "",
        "gols": [],
        "total": 0
    }

    nome = str(input("Nome do Jogador: "))
    partidas = int(input(f"Quantas partidas {nome} jogou? "))

    for c in range(partidas):
        gols = int(input(f"Quantos gols na partida {c + 1}? "))
        informacao["gols"].append(gols)
        informacao["total"] += gols

    informacao["nome"] = nome
    jogadores.append(informacao.copy())

    continuar = str(input("Quer continuar? [S/N] ")).upper().strip()[0]

    while continuar not in "SN":
        continuar = str(input("Caracter não conhecido. Quer continuar? [S/N] ")).upper().strip()[0]

    if continuar == "N":
        break

print("=" * 50)
print(f"{'COD':<5}{'NOME':<15}{'GOLS':<20}{'TOTAL'}")
print("=" * 50)

for i, j in enumerate(jogadores):
    print(f"{i:<5}{j['nome']:<15}{str(j['gols']):<20}{j['total']}")

print("=" * 50)

while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para parar) "))

    if busca == 999:
        break

    if busca < 0 or busca >= len(jogadores):
        print("ERRO! Não existe jogador com esse código.")
    else:
        print(f"-- LEVANTAMENTO DO JOGADOR {jogadores[busca]['nome']}")
        for p, g in enumerate(jogadores[busca]['gols']):
            print(f"   No jogo {p + 1} fez {g} gols.")
        print("-" * 30)

print("<< VOLTE SEMPRE >>")
