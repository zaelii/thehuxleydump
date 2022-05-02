a = float(input())
b = float(input())

pi = 3.14
area1 = (pi*(a**2))
area2 = (pi*(b**2))

if area1 > area2:
    print("Primeiro circulo")
if area1 < area2:
    print("Segundo circulo")
if area1 == area2:
    print("Iguais")

