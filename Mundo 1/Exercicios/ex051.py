## PA

primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razao: "))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(c, end=" -> ")