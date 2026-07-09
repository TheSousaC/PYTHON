##Função Contador
from time import sleep


def contador(inicio, fim, caminho):
    print("=" * 30)
    ##Se o caminho for 0, evita erro
    if caminho == 0:
        caminho = 1
    
    print(f"Contagem de {inicio} à {fim} de {caminho} em {caminho}")

    ##Ajuste para contagem decresente
    if inicio < fim:
        caminho = abs(caminho)
    elif inicio > fim:
        caminho = -abs(caminho)

    for c in range(inicio, fim + (1 if caminho > 0 else -1), caminho):
        print(c, end=' ')
        sleep(0.8)
    print()


contador(1, 10, 1)
contador(10, 0, 2)

print("Sua vez de personalizar a contagem!")
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
caminho = int(input("Caminho: "))
contador(inicio, fim, caminho)
