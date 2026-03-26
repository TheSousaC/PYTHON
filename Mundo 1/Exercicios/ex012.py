#Promoção / Calculo com Porcentagem

Preco = float(input('Qual o Preço do prduto? R$'))

NovoPreco = Preco - (Preco * 5 / 100)
print('O produto que vale R${:.2f} com um desconto de 5% fica no valor de R${:.2f}'.format(Preco, NovoPreco))