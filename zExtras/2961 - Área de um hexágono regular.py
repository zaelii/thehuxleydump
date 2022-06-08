import math

lado = float(input())

lado_hexagono = lado
area_hexagono = (((lado**2)*(math.sqrt(3))/4)*6)
perimetro = lado*6





print("Lado do hexagono: {:.1f} metros,".format(lado_hexagono))
print("Area: {} metros quadrados,".format(area_hexagono))
print("Perimetro: {:.1f} metros.".format(perimetro))
