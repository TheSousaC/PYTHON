# Auemnto/Acrescimo %

Salario = float(input('Qual o seu salario: R$'))

Novo = Salario + (Salario * 15 / 100)

print('Você ganha R${:.2f}, mas com um acrescimo de 15% passará a ganhar {:.2f}'.format(Salario, Novo))