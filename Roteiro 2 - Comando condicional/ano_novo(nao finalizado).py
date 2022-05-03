dia1 = int(input())
CO, RE, DE = map(float, input().split())
dia2 = int(input())
CO2, RE2, CE, DE2 = map(float, input().split())

if 1 <= dia1 <= 24:
    soma1 = CO + RE + DE
    print("Compras de natal: R$ {:.2f}".format(soma1))
elif 25 <= dia1 <= 31:
    soma2 = CO2 + RE2 + CE + DE2
    print ("Compras de ano novo: R$ {:.2f}".format(soma2))
if 25 <= dia2 <= 31:
    soma3 = CO2 + RE2 + CE + DE2
    print ("Compras de ano novo: R$ {:.2f}".format(soma3))
elif 1 <= dia2 <= 24:
    soma4 = CO + RE + DE
    print("Compras de natal: R$ {:.2f}".format(soma4))
