## Media de notas

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f"\033[1;32mAprovado!!!\n\033[0;0mSua média foi de \033[1;32m{media:.2f}")
elif media <= 6.9 and media >= 5:
    print(f"\033[1;31mRecuperação\n\033[0;0mSua média foi de \033[1;31m{media:.2f}")
else:
    print(f"\033[1;32mReprovado\n\033[0;0mSua media foi de \033[1;31m{media:.2f}")