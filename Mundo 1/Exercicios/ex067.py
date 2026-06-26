## tabuada top

numero = 0

while numero > -1:
    numero = int(input("De que tabuada vc deseja ver?\nR: "))
    cont = 0
    print("-"*10)
    while numero > -1:
        cont += 1
        print(f"{numero} x {cont} = {numero*cont}")
        if cont == 10:
            break

print("Fim do programa")
print("-"*10)