##Função Ficha dos jogadores
def ficha(nome="<deconhecido>", gols=0):
    if nome == "":
        nome = "<deconhecido>"
    if gols == "":
        gols = 0
    return f"O jogador {nome} fez {gols} gol(s)"


nome = str(input("Digite o nome: "))
goleadas = str(input("Digite o gols: "))

resp = ficha(nome, goleadas)
print(resp)
