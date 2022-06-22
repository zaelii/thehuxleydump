dia = 0
total_de_cartas = 0

for entregadas in range(0,7):
    cartas = int(input())
    total_de_cartas = total_de_cartas + cartas
    if cartas >= 100:
        dia += 1

print(dia)
print(round(total_de_cartas/7))
