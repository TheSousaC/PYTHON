##Guardar valores em uma tupla

valores = int(input("Digite o primeiro numero: ")), int(input("Digite o segundo número: ")), int(input("Digite o Terceiro número: ")), int(input("Digite o quartp numero: "))
print("=" * 30)

cont = 0
nove = valores.count(9)

print(f"Os números digitados foram: {valores}")
print(f"O Valor 9 apareceu {valores.count(9)} vezes")
if 3 in valores:
    print(f"O numero 3 está na posição {valores.index(3) + 1}")
else:
    print("O número 3 não aparece na tupla")

print("Os números pares digitados foram: ", end='')

for n in valores:
    if n % 2 == 0:
        print(f"{n}", end=' ')
