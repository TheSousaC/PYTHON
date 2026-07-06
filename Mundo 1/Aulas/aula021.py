##Mais Funções

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial(3)
f4 = fatorial(2)
f5 = fatorial(10)

print(f"O fatorial de cada um é {f1}, {f2}, {f3}, {f4} e {f5}")
