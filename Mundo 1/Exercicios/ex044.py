## Calcular valor sobre produto. Considerando o preço e condição a ser pago

print("-=-" * 20)
print("-=-=-=-=-=-=-Compre HERE-=-=-=-=-=-=-")
print("-=-" * 20)
nome = str(input("Digite seu nome: "))
nome_Produto = str(input("Digite o nome do produto: "))
preco = float(input("Digite o valor do produto: "))
condicao = int(input("Digite o condicao do produto:\n1:À Vista(Dinheiro ou Cheque)\n2:Pix\n3:À Vista no Cartão\n4:Duas Vezes no Cartão\n5:Três vezes ou mais no cartão\nQual opção você prefere? "))

if condicao == 1:
    preco = preco - (preco * 0.10)
    print(f"Você pagará R${preco:.2f} (10% de desconto)")
elif condicao == 2:
    preco = preco - (preco * 0.20)
    print(f"Ao pagar no Pix você recebe 20% de desconto. O total será de R${preco:.2f}")
elif condicao == 3:
    preco = preco - (preco * 0.05)
    print(f"Ao pagar a Vista no Cartão receberá 5% de desconto. O total será de R${preco:.2f}")
elif condicao == 4:
    preco_parcela = preco / 2
    print(f"Ao pagar 2 vezes no cartão você não recebe desconto. Cada parcela custará {preco_parcela:.2f}")
elif condicao == 5:
    preco_parcela = preco / 3
    print(f"Ao pagar 3 vezes no cartão você não recebe desconto. Cada parcela custará {preco_parcela:.2f}")
else:
    print("Número não encontrado.")