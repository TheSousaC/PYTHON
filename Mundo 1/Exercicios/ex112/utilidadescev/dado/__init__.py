def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(",", ".").strip()
        if entrada.isalpha() or entrada == "":
            print(f"Erro! \"{entrada}\" não é um preço válido")
        else:
            valido = True
            return float(entrada)