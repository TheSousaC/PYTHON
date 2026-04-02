# Verificação do "a"

Frase = input("Digite uma frase bonita: ")

if Frase.lower().count('a') > 0:
    print(f"Na frase exite {Frase.lower().count('a')} 'a' s\n"
          f"O primeiro 'a' se encontra em {Frase.find('a')}\n"
          f"E o ultimo se encontra em {Frase.rfind('a')}")