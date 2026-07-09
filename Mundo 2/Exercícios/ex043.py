## IMC
from math import pow

nome = str(input("Digite seu nome: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / pow(altura, 2)

if imc < 18.5:
    print(f"Seu IMC é: {imc}\nVocê está abaixo do peso, busque subir seu peso {nome}")
elif imc >= 18.5 and imc < 25:
    print(f"Seu IMC é: {imc}\nVocê está no peso ideal, parabens {nome}!")
elif imc >= 25 and imc < 30:
    print(f"Seu IMC é: {imc}\nVocê está no sobrepeso, cuidado {nome}!")
else:
    print(f"Seu IMC é {imc}\nEita, você está na Obesidade mórbida, cuidado {nome}!!!!!!!!")