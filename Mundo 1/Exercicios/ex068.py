## par ou impar

from random import randint
vitorias = 0
record = vitorias
numero = 0
soma = 0

computador = randint(0, 100)
print("Sou seu computador, tente adivinhar se eu pensei em um número impar ou par. HAHAHAHAHAHHAHAHHAHAHAHAHA")

while True:
    palpite = str(input("Qual você escolhe? [P/I]: ")).strip().upper()[0]
    numero = int(input("Digite um valor: "))
    soma = numero + computador
    if palpite == "P" and soma % 2 == 0 or palpite == "I" and soma % 2 != 0:
        print("Você acertou uma, parabens...\nVamos de novo")
        vitorias += 1
        if vitorias > record:
            record = vitorias
    elif palpite == "P" and soma % 2 != 0 or palpite == "I" and soma % 2 == 0:
        print("Você errou HAHAHAHAHAHA")
        break

if vitorias == 1:
    print(f"Você apenas teve {vitorias} vitoria.")
elif vitorias >= 2:
    print(f"Você teve uma sequência de {vitorias} vitorias.\nSeu recorde foi de {record}")
