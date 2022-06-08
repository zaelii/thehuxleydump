print("Digite um numero:")

n = int(input())

if n >= 0:
    u = n % 10
    print ("Algarismo das unidades: "+str(u))
if n < 0:
    n = n*-1
    u = n % 10
    print ("Algarismo das unidades: "+ str((u-u*2)))


