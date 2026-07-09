##Aprimorando a matriz HEHEHEHHEHEHEHEHE

matriz = []
somaColuna = somaPares = maiorValor = 0
# =)
# =(
# :)
# :(

x = y = 0
for c in range(0, 9):
    matriz.append(int(input(f"Digite um numero na posição [{y},{x}]: ")))
    if x <= 3:
        x += 1
    if x == 3:
        x = 0
        y += 1
for numero in matriz[:3]:
    print(f"[ {numero} ]", end="")
print()
for numero in matriz[3:6]:
    print(f"[ {numero} ]", end="")
print()
for numero in matriz[6:9]:
    print(f"[ {numero} ]", end="")

print()
for numero in matriz:
    if numero % 2 == 0:
        somaPares += numero

print(f"A soma dos números pares digitados é de: {somaPares}")

numero1 = matriz[2]
numero2 = matriz[5]
numero3 = matriz[8]
somaColuna = numero1 + numero2 + numero3

print(f"A soma dos números da coluna 3 é de: {somaColuna}")

if matriz[3] > matriz[4] > matriz[5]:
    maiorValor = matriz[3]
elif matriz[4] > matriz[3] > matriz[5]:
    maiorValor = matriz[4]
else:
    maiorValor = matriz[5]

print(f"O maior valor da segunda linha é: {maiorValor}")