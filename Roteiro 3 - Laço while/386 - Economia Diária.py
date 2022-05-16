#Feito

i = 0
cumpriu = 0
aux = float(input()) 
soma = aux

while(True): 
    if(i != 6): 
        x = float(input())
        soma += x
        if(x >= aux+0.50):
            cumpriu += 1
        aux = x 
    else:
        break
    i += 1

print("R$ {:.2f}".format(soma))
print(cumpriu)
