## Ler numeros e retornar o maior e menor

number1 = int(input("Digite o primeiro numero: "))
number2 = int(input("Digite o segundo numero: "))
number3 = int(input("Digite o terceiro numero: "))

if number1 > number2 and number1 > number3:
    print(f"O maior número é {number1}")
elif number2 > number1 and number2 > number3:
    print(f"O maior número é {number2}")
elif number3 > number1 and number3 > number2:
    print(f"O maior número é {number3}")

if number1 < number2 and number1 < number3:
    print(f"O menor número é {number1}")
elif number2 < number1 and number2 < number3:
    print(f"O menor número é {number2}")
elif number3 < number1 and number3 < number2:
    print(f"O menor número é {number3}")
