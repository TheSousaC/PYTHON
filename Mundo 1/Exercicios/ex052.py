## Primos ou não

num = int(input("Digite um número inteiro: "))

primo = True

if num <= 1:
    primo = False
else:
    for c in range(2, num):
        if num % c == 0:
            primo = False
            break

if primo:
    print("É primo")
else:
    print("Seu número não é primo")


## Ver a explicação