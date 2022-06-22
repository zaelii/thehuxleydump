comida = input().lower()
bebida = input().lower()
total = 0.0
pLasanha = 8.00
pEstrogonofe = 11.00
pRefrigerante = 3.00
pSuco = 2.50

if comida == 'lasanha': 
    if bebida == 'refrigerante':
        total = pLasanha + pRefrigerante
    else:
        total = pLasanha + pSuco
elif comida == 'estrogonofe': 
    if bebida == 'refrigerante':
        total = pEstrogonofe + pRefrigerante
    else:
        total = pEstrogonofe + pSuco

print("{:.2f}".format(total))