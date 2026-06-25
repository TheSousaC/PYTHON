## Só pode hetero

sexo = " "

while sexo != "M" and sexo != "F":
    sexo = str(input("Digite seu sexo: [M/F] ")).upper()
    if sexo != "M" and sexo != "F":
        print(f"{sexo} invalido, digite apenas M ou F")
print("Sexo registrado com sucesso!")