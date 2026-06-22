## Base de conversão

number = int(input("Digite um número inteiro: "))
base = int(input("Converta em\n1:Binário\n2:octal\n3:hexadecimal\nQual a base que você quer converter? "))

if base == 1:
    number_bin = bin(number)
    print(f"{number} em binario é: {number_bin[2:]}")
elif base == 2:
    number_oct = oct(number)
    print(f"{number} em octal é: {number_oct[2:]}")
elif base == 3:
    number_hex = hex(number)
    print(f"{number} em hexadecimal é: {number_hex[2:]}")
else:
    print("Numero invalido")