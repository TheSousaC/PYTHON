##Função leiaInt()

def leiaInt(msg):
    while True:
        numero = input(msg)
        if numero.isnumeric():
            return int(numero)
        else:
            print("\033[31;1mERRO! Digite um número inteiro válido!\033[m")


n = leiaInt("Digite aqui um número: ")
print(f"Você acabou de digitar o número {n}")
