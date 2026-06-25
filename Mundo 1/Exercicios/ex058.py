## Melhorando o ex028
from random import randint

print("-=-" * 10)
print("Vou pensar em um numero entre 0 e 10\nAdivinhe... Se for capaz")
print("-=-" * 10)

tentativas = 0
chute = 0
computador = randint(0, 10)

while chute != computador:
    chute = int(input("Digite um numero entre 0 e 10: "))
    if chute != computador:
        tentativas += 1
        print("Tente novamente hehehehe")
print(f"Você acertou!!! O computador também pensou em {computador}\nAo todo foram necessarias {tentativas} tentativas")