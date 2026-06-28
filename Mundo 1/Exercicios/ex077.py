##Verificador de Vogais

palavras = "casa", "livro", "computador", "janela", "escola", "carro", "telefone", "python", "programacao", "teclado", "mouse", "internet", "cidade", "praia", "montanha", "amigo", "familia", "trabalho", "viagem", "musica"

for p in palavras:
    print(f"\nNa palavra {p.upper()} temos: ", end="")
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end=" ")