#Aluguel

Dias = int(input('Por quantos dias o carro foi alugado? '))
Km = float(input('Quantos Km foram percorridos? '))

Preco = (Dias * 60) + (Km * 0.15)
Aredondado = round(Preco, 2)

print(f'O preço pela quantidade de dias e km rodados é de R${Aredondado}')


# Arredondando o valore usando nov formatação