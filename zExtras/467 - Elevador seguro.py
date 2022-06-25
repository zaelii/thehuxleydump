acumulador = 0
n_max = 0  


while True:
    peso = int(input())
    acumulador = acumulador + peso
    n_max += 1
    if peso == 0:
        n_max = n_max - 1
        break
    else:
        if n_max > 7:
            acumulador = acumulador - peso
            n_max = n_max - 1
            break
        elif acumulador > 560:
            n_max = n_max - 1
            acumulador = acumulador - peso
            break

print(n_max)
print("{:.1f}".format(acumulador))

