raio = float(input())
graus = float(input())
pi = 3.14

Comprimento = raio*pi*graus/180
Area = pi * raio**2 * graus /360


print ("{:.2f}".format(Comprimento))
print ("{:.2f}".format(Area))
