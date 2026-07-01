##MEGA SENA
from time import sleep
from random import randint

print("="*40)
print("MEGA SENA".center(40))
print("="*40)

sorteio = []
jogo = []
jogadas = int(input("Quantos jogos deseja sortear? "))

for c in range(jogadas):
    while len(jogo) < 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    jogo.sort()
    sorteio.append(jogo[:])
    jogo.clear()
    print(sorteio)