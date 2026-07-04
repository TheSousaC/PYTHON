##Carteira de trabalho
from datetime import date

cadastro = {
    "nome": "",
    "idade": 0,
    "ctps": 0
}
atual = date.today().year

cadastro["nome"] = str(input("Qual o seu nome? "))
ano_nasc = int(input("Qual o ano de nascimento? "))
cadastro["idade"] = atual - ano_nasc
carteira = int(input("Carteira de trabalho [Digite 0 se não tem]: "))

if carteira == 0:
    print(carteira)
    print("=" * 30)
    print(f"Nome tem o valor de: {cadastro['nome']}")
    print(f"Idade tem o valor de: {cadastro["idade"]}")
    print(f"Ctps tem o valor de: {cadastro["ctps"]}")

cadastro["contratacao"] = int(input("Ano de contratação: "))
cadastro["salario"] = float(input("Salário: "))

aposentadoria = cadastro["idade"] + ((cadastro["contratacao"] + 35) - atual)

print(carteira)
print("=" * 30)
print(f"Nome tem o valor de: {cadastro['nome']}")
print(f"Idade tem o valor de: {cadastro["idade"]}")
print(f"Ctps tem o valor de: {cadastro["ctps"]}")
print(f"Contratação tem o valor de: {cadastro['contratacao']}")
print(f"Salário tem o valor de: {cadastro['salario']}")
print(f"Aposentadoria em {aposentadoria}")
