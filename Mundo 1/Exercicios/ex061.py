## refazendo o ex051

initial_term = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
termo = initial_term
contador = 1
while contador <= 10:
    print(f"{termo} -> ", end="")
    termo += razao
    contador += 1

print("FIM")