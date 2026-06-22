from datetime import date

data = date.today().year

ano_nasc = int(input("Qual o ano de nascimento? "))
idade = data - ano_nasc

if idade == 18:
     print("Você já pode se alistar")
elif idade <= 17:
    print("Ainda vai se alistar")
else:
    print("Já passou da hora de se alistar")
