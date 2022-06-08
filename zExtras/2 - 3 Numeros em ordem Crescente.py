a = int(input())
b = int(input())
c = int(input())

if a < b < c:
    print (a)
    print (b)
    print (c)
elif a < c < b:
    print (a)
    print (c)
    print (b)
elif b < a < c:
    print (b)
    print (a)
    print (c)
elif b < c < a:
    print (b)
    print (c)
    print (a)
elif c < a < b:
    print (c)
    print (a)
    print (b)
else:
    print (c)
    print (b)
    print (a)

#4 errors
#10 passed
