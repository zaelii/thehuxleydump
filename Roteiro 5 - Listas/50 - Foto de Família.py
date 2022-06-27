qtde = 4

lista = []

for i in range(qtde):
    pessoa = float(input())
    lista.append(pessoa)

lista.sort()
print("{:.2f}".format(lista[0]))
print("{:.2f}".format(lista[2]))
print("{:.2f}".format(lista[3]))
print("{:.2f}".format(lista[1]))