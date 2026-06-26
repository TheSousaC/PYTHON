## LOJINHA TOPZERA

nome = ""
preco = 0
total = 0
MaiorPreco = 0
barato = 0
nomeProdutoBarato = ""
continuar = ""
repetidor = 0
print('=' * 20)
print("  LOJINHA TOPZERA ")
print('=' * 20)

while True:
    nome = str(input("Nome do produto: "))
    preco = float(input(f"Digite o preço de {nome}: R$"))
    continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    repetidor += 1
    total += preco
    if preco > 1000:
        MaiorPreco += 1
    if repetidor == 1:
        barato = preco
        nomeProdutoBarato = nome
    if preco < barato:
        barato = preco
        nomeProdutoBarato = nome
    if continuar == "N":
        break
print("=" * 20)
print(f"O total da compra foi R${total:.2f}")
print(f"O produto mais barato é o {nomeProdutoBarato}, custando R${barato:.2f}")
print(f"{MaiorPreco} produtos custam mais de R$1000")