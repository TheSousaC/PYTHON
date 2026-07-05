##Fução área

def area(l, c):
    area = l * c
    print(f"A área de um terreno {l}X{c} é de {area}²")


print("Controle de Terrenos")
print("-" * 20)

largura = float(input("Largura (m): "))
comprimento = float(input("Comprimento (m): "))
area(largura, comprimento)
