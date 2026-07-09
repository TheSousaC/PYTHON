##Ex 104 melhorado e add funcionalidades

def leiaInt(msg):
    while True:
        numero = str(input(msg))
        try:
            inteiro = int(numero)
            return inteiro
        except (ValueError, TypeError):
            print("Erro! Digite um número inteiro valido")


def leiaFloat(msg):
    while True:
        numero = str(input(msg))
        try:
            real = float(numero)
            return real
        except (ValueError, TypeError):
            print("Erro! Digite um número real valido")


inteiro = leiaInt("Digite um número inteiro: ")
real = leiaFloat("Digite um número real: ")
print(f"O valor inteiro digitado foi {inteiro} e o real foi {real}")
