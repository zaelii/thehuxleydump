x = int(input())

if x == 1:
    print ("Nordeste")   
elif x == 2:
    print ("Norte")
elif x == 3 or x == 4:
    print ("Centro-Oeste")
elif x >= 5 and x <= 9:
    print ("Sul")
elif x >= 10 and x <= 15:
    print ("Sudeste")
