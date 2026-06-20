nome = str(input("Digite seu nome: "))
if nome == "Gabriel":
    print("Eae bonitão?")
else:
    print("Que nome bonito tbm")
print(f"Bom dia {nome}")

n1 = int(input("Digite sua primeira nota: "))
n2 = int(input("Digite sua segunda nota: "))

media = (n1 + n2) / 2

if media >= 5:
    print(f"Aprovado, sua média foi {media}")
else:
    print(f"Reprovado, sua media foi de {media}")