divida = int(input())
salario = int(input())

while True:
    resto = divida - salario
    print ("(antes) "+str(divida))
    if resto <= 0:
        print("(depois) 0")
        break
    if resto > 0:
        print("(depois) "+str(resto))
        divida = resto
