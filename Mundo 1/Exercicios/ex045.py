## Pedra papel e tesoura
from random import randint
print('-' * 20)
print("PEDRA, PAPEL E TESOURA")
print('-' * 20)

computador = randint(1, 3)
opcao = int(input("Escolha:\n1:Pedra\n2:Papel\n3:Tesoura\n"))

if ((opcao == 1 and computador == 1) or (opcao == 2 and computador == 2) or (opcao == 3 and opcao == 3)):
    print("Você perdeu!")
else:
    print("Você ganhou!!!!")