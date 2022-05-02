dias = int(input())
kmTotal = int(input())

diaria = 90
maxKm = 100*dias
gasto = (kmTotal-maxKm)*12+diaria*dias 

if kmTotal>maxKm:
    print("{:.2f}".format(gasto))
else:
    print("{:.2f}".format(diaria*dias))