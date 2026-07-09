## Contagem regressiva

from time import sleep

contagem = int(input("Digite em segundos a contagem regressiva para o lançamento de fogos de artifíco: "))

for c in range(contagem, 0, -1):
    print(c)
    sleep(1)
print("\033[1;31mBUM")