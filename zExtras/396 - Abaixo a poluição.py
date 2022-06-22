total = 0
casas = 0
multa = 0

while True:
    carros = int(input())
    if carros == 999:
        break
    else:
        if carros > 2:
            total = carros + total - 2
            casas += 1
            multa = total*12.89
print("{:.2f}".format(multa))
print(casas)
    