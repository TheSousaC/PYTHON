##Sorteio de uma dado a 4 jogadores
from operator import itemgetter  ##Sla oq é isso, mas vou aprender na correção
from random import randint
from time import sleep

jogadores = {"jogador 1": randint(1, 6),
             "jogador 2": randint(1, 6),
             "jogador 3": randint(1, 6),
             "jogador 4": randint(1, 6)
             }

for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

print("=" * 30)
print("Ranking dos jogadores".center(30))
print("=" * 30)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
contador_topzera = 1

for c in ranking:
    print(f'{contador_topzera}° lugar: {c[0]} com {c[1]}')
    contador_topzera += 1
    sleep(1)
