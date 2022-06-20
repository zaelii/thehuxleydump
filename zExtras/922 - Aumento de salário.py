salario = float(input())

vinte_porcento = salario+(salario*0.2)
quinze_porcento = salario+(salario*0.15)
dez_porcento = salario+(salario*0.1)
cinco_porcento = salario+(salario*0.05)


if salario <= 280: 
    print("{:.2f}".format(vinte_porcento))
elif 280 < salario <= 700:
    print("{:.2f}".format(quinze_porcento))
elif 700 < salario <= 1500:
    print("{:.2f}".format(dez_porcento))
else:
    print("{:.2f}".format(cinco_porcento))