altura = float(input())
raio = float(input())
pi = 3.14

volume = pi * (raio**2) * altura
superficie = (2*pi) * raio * altura + (2*pi) * (raio**2)


print("{:.2f}".format(volume))
print("{:.2f}".format(superficie))
