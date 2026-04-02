# Ler nome e Mostrar ele alterado

Nome = input("Digite seu Nome Completo: ")

print(f"Maiusculo: {Nome.upper()}\n"
      f"Minusculo: {Nome.lower()} \n"
      f"Quantas Letras sem espaço: {len(Nome.replace(" ", ""))}\n"
      f"Quantas letra tem o 1° nome: {len(Nome.split()[0])}")