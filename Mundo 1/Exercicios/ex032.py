## Verificador de ano bissexto (como faz isso?)
from datetime import date
ano = int(input("Qual ano você quer verificar? Coloque 0 para verificar o ano atual"))
if ano == 0:
    ano = date.today().year
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f"O ano {ano} é BISSEXTO")
    else:
        print(f"{ano} Não é bissexto")