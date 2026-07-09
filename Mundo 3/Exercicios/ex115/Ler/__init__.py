def lerArquivo():
    with open("Arquivo/lista.txt", "r", encoding="utf-8") as Arquivo:
        for linha in Arquivo:
            print(linha.strip())