#Conversor de Temperatura

Celcios = float(input('Qual é a temperatura em C°: '))

Faharenheit = (Celcios * 1.8) + 32
Kelvin = Celcios + 273.15

print('A temperatura {:.1f}C° em Fahrenheit é {:.1f}F° e em Kelvin é {:.2f}K°'.format(Celcios, Faharenheit, Kelvin))