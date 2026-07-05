##Função de verificar o maior
from time import sleep


def maior(*num):
    print("-" * 30)
    print("Analisando os valores passados...")
    sleep(0.8)
    for c in num:
        print(f"{c} ", end="")
    print(f"Foram informados {len(num)} valores.")
    sleep(0.8)
    print(f"O maior valor informado foi {max(num)}")
    sleep(0.8)


valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
maior(*valores)
valores = [10, 20, 0, 100, 1000000, 60]
maior(*valores)
valores = [0]
maior(*valores)
