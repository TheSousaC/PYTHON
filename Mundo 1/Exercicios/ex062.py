## PA Melhorado 2.0

initial_term = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
termo = initial_term
contador = 1
total = 0
mais =10
while mais != 0:
    total += mais
    while contador <= total:
        print(f"{termo} -> ", end="")
        termo += razao
        contador += 1
    print("Pausa")
    mais = int(input('Quantos termos deseja acrescentar? '))
print(f'Progressão finalizada com {total} termos')
