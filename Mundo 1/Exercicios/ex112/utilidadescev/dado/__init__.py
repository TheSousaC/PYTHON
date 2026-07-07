from Exercicios.ex112.utilidadescev import moeda
def leiaDinheiro(msg):
    while True:
        p = (input(msg))
        if p.isnumeric():
            ##Retorna e formato BR
            return float(p.replace(',', '.'))
        else:
            print(f"ERRO! '{p}' não é valido")
