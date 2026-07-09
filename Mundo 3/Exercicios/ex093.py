##Aproveitamento de um jogador

informacao = {
    "nome": " ",
    "gols": [],
    "total": 0
}

nome = str(input("Nome do Jogador: "))
partidas = int(input(f"Quantas partidas {nome} Jogou? "))
for c in range(0, partidas):
    gols = int(input(f"Quantos gols na partida {c + 1}? "))
    informacao["gols"].append(gols)
    informacao["total"] += gols
informacao["nome"] = nome

print("=" * 30)
print(informacao)
print("=" * 30)

print(f"O campo Nome tem o valor {informacao['nome']}")
print(f"O campo Gols tem o valor {informacao['gols']}")
print(f"O campo Total tem o valor {informacao['total']}")
print("=" * 30)

print(f"O jogador {informacao['nome']} jogou {len(informacao["gols"])} partidas")
for p, g in enumerate(informacao["gols"]):
    print(f" => Na partida {p + 1}, fez {g} gols")
