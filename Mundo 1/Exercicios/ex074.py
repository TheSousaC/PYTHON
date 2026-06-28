## Números sorteados
from random import randint

sorteio = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)

print(f"os numeros sorteados foram: {sorteio}")
print(f"O maior dentre eles é: {max(sorteio)}")
print(f"O menor dentre eles é {min(sorteio)}")