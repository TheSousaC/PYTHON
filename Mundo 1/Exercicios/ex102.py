##Função Fatorial

def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número
    :param n: O numero inteiro
    :param show: (Opcional) Mostrar ou não a conta (True or False)
    :return: O valor Fatorial de um número n
    """
    f = 1
    if show == True:
        for i in range(n, 0, - 1):
            f *= i
            print(f"{i}", "=" if i == 1 else "X", end=" ")
        return f
    else:
        for c in range(n, 0, -1):
            f *= c
        return f


# print(fatorial(10, True))
# help(fatorial)
