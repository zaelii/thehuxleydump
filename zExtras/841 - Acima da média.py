a = float(input())
b = float(input())
c = float(input())
n_acima_media = 0

if a >= 7 and b >= 7 and c >= 7:
    print("3")
elif a >= 7 and b >= 7 and c < 7:
    print("2")
elif a >= 7 and c >= 7 and b < 7:
    print("2")
elif b >= 7 and c >= 7 and a < 7:
    print("2")
elif a >= 7 and b < 7 and a < 7:
    print("1")
elif b >= 7 and a < 7 and c < 7:
    print("1")
else:
    print("1")

#2 errors
#4 passed
