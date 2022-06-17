#841 - Acima da média

a = float(input())
b = float(input())
c = float(input())

if (a <= 10 and b <= 10 and c <= 10):
    if ((a >= 7) and (b >= 7) and (c >= 7)):
        print(3)
    elif ((a >= 7) and (b >= 7) and (c < 7)):
        print(2)
    elif ((a >= 7) and (b < 7) and (c >= 7)):
        print(2)
    elif ((a < 7) and (b >= 7) and (c >= 7)):
            print(2)
    elif ((a >= 7) or (b >= 7) or (c >= 7)):
            print(1)
else:
    print("Nenhuma nota acima da média")
