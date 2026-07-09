## verificador de palindromo

frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print(f"A frase {frase} ao inverso fica {inverso}\nÉ um palindromo")
else:
    print(f"A frase {frase} ao contrario fica: {inverso}\nNão é um palindromo")