print("Digite a base menor:")
base_menor = int(input())
print("Digite a base maior:")
base_maior = int(input())
print("Digite a altura:")
altura = int(input())

area_trapezio = ((base_maior + base_menor)*altura)/2

print("Area do trapezio: "+"{:.6f}".format(area_trapezio))
