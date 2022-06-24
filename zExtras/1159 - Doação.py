import math

doacao = int(input())

divisoria = doacao/3
sobra = doacao % 3

print(math.floor(divisoria))
print(sobra)

