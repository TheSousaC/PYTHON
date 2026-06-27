## Tabuada Topzera

while True:
    n = int(input("Quer ver a tabuada de que número? "))
    if n < 0:
        break
    print("=" * 20)
    for c in range(1, 11):
        print(f"{n} X {c} = {n * c}")
    print("=" * 20)
print("=" * 20)
print("Fim do programa, volte sempre.")
print("=" * 20)