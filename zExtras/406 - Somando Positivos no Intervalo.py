n1 = int(input())
n2 = int(input())

total = 0
if n2>n1:
    for numeros in range(n1,n2+1):
        if numeros > 0:
            total = numeros + total

if n1>n2:
    for numeros in range(n2,n1+1):
        if numeros > 0:
            total = numeros + total

print(total)