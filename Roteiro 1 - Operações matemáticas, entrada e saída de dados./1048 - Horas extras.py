salario_base = float(input())
horas_extras = int(input())


valor_extra = horas_extras * (salario_base/44) * 1.1
valor_pagar = valor_extra + salario_base


print("{:.2f}".format(valor_pagar))

