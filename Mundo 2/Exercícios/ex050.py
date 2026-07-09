## Leitor e somador de pares

s = 0
for c in range(1, 7):
    num =  int(input(f"Digite o {c}° numero inteiro: "))
    if num % 2 == 0:
        s += num
print(f"A soma de todos o numeros pares digitados foi: {s}")