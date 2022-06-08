#2330 - Eh par ou ímpar?

n = int(input())
resto = n % 2

if resto == 0:
    print("O numero eh {} e ele eh par".format(n))
else:
    print("O numero eh {} e ele eh impar".format(n))