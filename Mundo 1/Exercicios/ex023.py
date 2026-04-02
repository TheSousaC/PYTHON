#Ler um numero e mostrar tudo

Numero = input("Digite um numero de 0 a 9999: ")

if len(Numero) == 4:
    print(f"Unidade: {Numero[3]}\n"
          f"Dezena: {Numero[2]}\n"
          f"Centena: {Numero[1]}\n"
          f"Milhar: {Numero[0]}")
elif len(Numero) == 3:
    print(f"Unidade: {Numero[2]}\n"
          f"Dezena: {Numero[1]}\n"
          f"Centena: {Numero[0]}")
elif len(Numero) == 2:
    print(f"Unidade: {Numero[1]}\n"
          f"Dezena: {Numero[0]}")
elif len(Numero) == 1:
    print(f"Unidade: {Numero[0]}")