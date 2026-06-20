from random import randint
numero = randint(1, 5)

usuario_res  = int(input("O computador pensou em um número, qual é esse número (de 1 a 5)? "))

if usuario_res == numero:
    print(f"VOCÊ ACERTOU!!!!\nO numero escolhido foi: {numero}")
else:
    print("Errou feio, igual naquele dia, igual aqueles dias, melhore.")