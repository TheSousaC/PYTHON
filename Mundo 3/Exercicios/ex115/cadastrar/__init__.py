from time import sleep
def cadastrar():
    print("-"*30)
    print("Cadastrando uma Pessoa".center(30))
    print("-"*30)

    nome = str(input("Digite o nome da pessoa: "))
    while True:
        try:
            idade = int(input("Digite a idade da pessoa: "))
        except ValueError:
            print(f"Erro no valor digitado. Digite a idade corretamente.")
        else:
            ##Escreve uma nova linha no arquivo lista.txt
            with open("Arquivo/lista.txt", "a", encoding="utf-8") as Arquivo:
                Arquivo.write(f"{nome} - {idade}\n")
            print(f"{nome} Cadastrado com sucesso!")
            sleep(1)
            break