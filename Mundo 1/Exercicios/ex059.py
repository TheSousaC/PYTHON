## Menu
from linecache import clearcache

valor1 = int(input("Digite um número inteiro: "))
valor2 = int(input("Digite outro numero inteiro: "))
opcao = 0
continuar = "S"
while opcao != 5:
    if continuar == "S":
        print("Menu Xuxu Beleza")
        print("[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos numeros\n[5] Sair")
        opcao = int(input("Digite uma opcao: "))
        if opcao == 1:
            soma = valor1 + valor2
            print(f"A soma de {valor1} e {valor2} é: {soma}\n")
            continuar = str(input("Deseja continuar? [S/N] ")).upper()
        elif opcao == 2:
            multiplicacao = valor1 * valor2
            print(f"A multiplicação de: {valor1} e {valor2} é {multiplicacao}\n")
            continuar = str(input("Deseja continuar? [S/N] ")).upper()
        elif opcao == 3:
            if valor1 > valor2:
                print(f"Dentre os dois o maior número é: {valor1}\n")
                continuar = str(input("Deseja continuar? [S/N] ")).upper()
            else:
                print(f"Dentre os dois o maior número é: {valor2}\n")
                continuar = str(input("Deseja continuar? [S/N] ")).upper()
        elif opcao == 4:
            valor1 = int(input("Para qual numero deseja trocar o primeiro valor? "))
            valor2 = int(input("Para qual numero deseja trocar o segundo valor? "))
            continuar = str(input("Deseja continuar? [S/N] ")).upper()
    else:
        opcao = 5
