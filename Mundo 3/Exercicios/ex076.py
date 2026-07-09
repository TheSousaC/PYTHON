## Lista de Preços

itens = "Caderno", 59.99, "Corretivo", 19.99, "Estojo", 14.99

print(f"-" * 40)
print(f"{'Loja do Precinho':^40}") ## É assim que centraliza
print(f"-" * 40)

for i in range(0, len(itens)):
    if i % 2 == 0:
        print(f"{itens[i]:.<30}", end="") ##Alinhar a esquerda e completar com "." pontinhos as 30 casas
    else:
        print(f"R${itens[i]:>5.2f}") ##Alinhar a direita e por duas casas decimais
print(f"-" * 40)
