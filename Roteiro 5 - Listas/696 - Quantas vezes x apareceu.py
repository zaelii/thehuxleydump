import collections

qtde = 10

lista = []

for i in range(qtde):
    n = int(input())
    lista.append(n)

repetidos = int(input())
print(collections.Counter(lista)[repetidos])
