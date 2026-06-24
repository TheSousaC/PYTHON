## verificador idade

from datetime import date

ano_nasc = 0
ano = date.today().year
menor = 0
maior = 0

for c in range(1, 8):
    ano_nasc = int(input(f"Digite o ano de nascimento da {c}° pessoa: "))
    idade = ano - ano_nasc
    if idade >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
print(f"Em um grupo de 7 amigos há entre eles {maior} pessoas maiores de 18 e {menor} pessoas menores de 18")