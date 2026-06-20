## Verificador de velocidade

velocidade = float(input("Qual a velocidade do carro? "))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f"Você passou do limite da rodovia, sua multa é de: R${multa}")
else:
    print("Certinho meu patrão, pode prosseguir")