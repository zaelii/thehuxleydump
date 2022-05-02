type = input()

if type == "a":
    a1 = int(input())
    a2 = int(input())
    a3 = int(input())
    ma = (a1+a2+a3)/3
    print(ma)
    if 70 <= ma <= 100:
        print("Aprovado")
    if 0 < ma < 40:
        print("Reprovado")
    if 40 <= ma <= 70:
        print("Final")
if type == "p":
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    p1 = int(input())
    p2 = int(input())
    p3 = int(input())
    mp = (((n1*p1) + (n2*p2) + (n3*p3)) / (p1 + p2 + p3))
    print ("p: ""{:.2f}".format(mp))
    if 70 < mp < 100:
        print("Aprovado")



