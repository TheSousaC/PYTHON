## Numeros por extenso

extenso = "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"

numero = int(input("Digite um numero inteiro de 0 a 20: "))

while numero > 20 or numero < 0:
    numero = int(input("Digite somente um numero entre 0 e 20: "))
print("Saiu do laço")

print(f"O número {numero} por extenso é: {extenso[numero]}")