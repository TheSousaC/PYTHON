# Ler angulo e calcular seno e cosseno e tangente

from math import cos, sin, tan, radians

Angulo = float(input("Digite um angulo qualquer: "))

RadAngulo = radians(Angulo)
Seno = sin(RadAngulo)
Cosseno = cos(RadAngulo)
Tangente = tan(RadAngulo)

print(f"O Seno de {RadAngulo:.2f}° é {Seno:.2f}")
print(f"O Cosseno de {RadAngulo:.2f}° é {Cosseno:.2f}")
print(f"O Tangente de {RadAngulo:.2f}° é {Tangente:.2f}")