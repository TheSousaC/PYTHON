##Verificar se tem () completas

expre = str(input("Digite uma expressão:"))
pilhas = []

for simb in expre:
    if simb == '(':
        pilhas.append('(')
    elif simb == ')':
        if len(pilhas) > 0:
            pilhas.pop()
        else:
            pilhas.append(')')
            break
if len(pilhas) == 0:
    print("Sua expressão é mt matematica")
else:
    print("Vá para humanas...")
