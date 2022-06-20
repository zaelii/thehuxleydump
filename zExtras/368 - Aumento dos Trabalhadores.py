salario = float(input())

dezporcento = salario+(salario*0.1)
seteporcento = salario+(salario*0.07)
cincoporcento = salario+(salario*0.05)


if salario > 500:
    print("{:.2f}".format(dezporcento))
elif salario > 300:
    print("{:.2f}".format(seteporcento))
else:
    print("{:.2f}".format(cincoporcento))