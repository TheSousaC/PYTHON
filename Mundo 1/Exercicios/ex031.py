## Preço da passagem de acordo com a distancia

distance = float(input("What is the distance (km/h) of your trip? "))

if distance <= 200:
    value = distance * 0.50
    print(f"Your trip will cost {value:.2f}")
else:
    value = distance * 0.45
    print(f"Your trip will cost {value:.2f}")