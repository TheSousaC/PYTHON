## Tabela do Brasileirão

# Tupla com os 20 times do Brasileirão 2026 ordenados da 1ª à 20ª posição
Tabela = "Palmeiras", "Flamengo", "Fluminense", "Athletico-PR", "Red Bull Bragantino", "Bahia", "Coritiba","São Paulo", "Atlético-MG", "Corinthians", "Cruzeiro", "Botafogo", "Vitória", "Internacional", "Santos", "Grêmio", "Vasco", "Remo", "Mirassol", "Chapecoense"

##Os 5 primeiros colocados
# print(Tabela[0:5])
contador = 1
print("=" * 30)
print("Os 5 primeiros colocados:")
for cont in range(0,5):
    print(f"{contador}° {Tabela[cont]}")
    contador += 1
print("=" * 30)

##Os 4 ultimos colocados
contador = 20
print("=" * 30)
print("Os ultimos 4 colocados:")
for cont in range(19, 15, -1):
    print(f"{contador}° {Tabela[cont]}")
    contador -= 1
print("=" * 30)

print("=" * 30)
print("Ordem Alfabetica: ")
print("=" * 30)
ordem = sorted(Tabela)
for posicao, cont in enumerate(ordem, start=1):
    print(f"{posicao}° {cont}")
print("=" * 30)

print("=" * 30)
print(f"Posição da Chapecoense: {Tabela.index("Chapecoense")+1}°")
