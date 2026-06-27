## Números sorteados
from random import randint
primeiro = randint(1, 10)
segundo = randint(1, 10)
terceiro = randint(1, 10)
quarto = randint(1, 10)
quinto = randint(1, 10)

sorteio = primeiro, segundo, terceiro, quarto, quinto

print(f"os numeros sorteados foram: {sorteio}")
print(f"O maior dentre eles é: {max(sorteio)}")
print(f"O menor dentre eles é {min(sorteio)}")