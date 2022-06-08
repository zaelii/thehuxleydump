import math

x, z = list(map(int, input().split()))

hogsmeade = ((x - 34)**2) + ((z - 220)**2)
dhogsmeade = math.sqrt(hogsmeade)

kakariko = ((x - 0)**2) + ((z - 0)**2)
dkakariko = math.sqrt(kakariko)

solitude = ((x - 140)**2) + ((z - 456)**2)
dsolitude = math.sqrt(solitude)



print("Distancia para Hogsmeade: {:.2f}".format(dhogsmeade))
print("Distancia para Kakariko: {:.2f}".format(dkakariko))
print("Distancia para Solitude: {:.2f}".format(dsolitude))
