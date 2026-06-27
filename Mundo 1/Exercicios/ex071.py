## Banco Topzera


print('='*20)
print("   Banco Topzera")
print('='*20)

num = int(input("Digite um valor pra sacar, digite um valor que termine com 0 ou 5: "))
total = num
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f"O total de {totced} de R${ced} ")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        totced = 0
        if total == 0:
            break