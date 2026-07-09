## Categorias de Natação

nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))

if idade <= 9:
    print("Você é Mirin")
elif idade <= 14:
    print("Você está naa categoria Infantil")
elif idade <= 19:
    print("Você está naa categoria Junior")
elif idade <= 20:
    print("Você está naa categoria Senior")
else:
    print("MASTER BLASTER")
