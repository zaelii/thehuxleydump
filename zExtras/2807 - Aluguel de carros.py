print("Digite a quantidade de dias de locacao:")
numero_dias = int(input())
print("Digite a quantidade de km rodados:")
km = int(input())

valor = ((numero_dias*30)+(km*0.01))
odesconto = (valor * 0.1)
total = (valor - odesconto)

print("Valor a pagar pelo aluguel: R$ "+"{:.6f}".format(total))