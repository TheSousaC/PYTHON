##Função Voto()
def voto(ano):
    from datetime import date
    atual = date.today().year
    global idade
    idade = atual - ano
    if idade < 16:
        return "VOTO NEGADO"
    elif idade >= 16 and idade < 18:
        return "VOTO OPCIONAL"
    elif idade >= 18 and idade < 65:
        return "VOTO OBRIGATORIO"
    else:
        return "VOTO OPCIONAL"


ano_nac = int(input("Digite o ano de nascimento: "))
resp = voto(ano_nac)
print(f"Com {idade} anos: {resp}")
