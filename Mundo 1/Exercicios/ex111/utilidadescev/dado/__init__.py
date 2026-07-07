from Exercicios.ex111.utilidadescev import moeda

def resumo(p, aument, dim):
    print(f"-" * 30)
    print(f"RESUMO DO VALOR".center(30))
    print(f"-" * 30)

    print(f"A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}")
    print(f"O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}")
    print(f"Aumentando {aument}%, temos: {moeda.aumentar(p, aument, True)}")
    print(f"Diminuindo {dim}%, temos: {moeda.diminuir(p, dim, True)}")
    print(f"-" * 30)