qtde = int(input())

lista = list(map(int, input().split()))


menor_valor = min(lista)
posicao = lista.index(menor_valor)

print("Menor valor: {}".format(menor_valor))
print("Posicao: {}".format(posicao))


