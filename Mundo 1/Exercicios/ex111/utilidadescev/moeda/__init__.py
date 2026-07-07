
def moeda(num):
    return f'R${num:.2f}'.replace('.', ',')


def metade(num, formato=False):
    if formato:
        return f"R${num / 2:.2f}".replace('.', ',')
    else:
        return num / 2


def dobro(num, formato=False):
    if formato:
        return f'R${num * 2:.2f}'.replace('.', ',')
    else:
        return num * 2


def aumentar(num, aum, formato=False):
    aumento = num + (num * aum / 100)
    if formato:
        return f'R${aumento:.2f}'.replace('.', ',')
    return aumento


def diminuir(num, dimin, formato=False):
    diminuicao = num - (num * dimin / 100)
    if formato:
        return f'R${diminuicao:.2f}'.replace('.', ',')
    else:
        return diminuicao