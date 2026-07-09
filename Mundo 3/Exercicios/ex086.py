##MATRIZ

matriz = []
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