#702 - Hipotenusa
import math

a = float(input())
b = float(input())

antes_hipotenusa = a**2 + b**2
hipotenusa = math.sqrt(antes_hipotenusa)

print("{:.2f}".format(hipotenusa))