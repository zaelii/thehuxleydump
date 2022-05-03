type = input()

if type == "a":
    a1 = int(input())
    a2 = int(input())
    a3 = int(input())
    ma = (a1+a2+a3)/3
    print("{:.2f}".format(ma))
    if 70 <= ma <= 100:
        print("Aprovado")
    elif 0 < ma < 40:
        print("Reprovado")
    elif 40 <= ma <= 70:
        print("Final")
    else:
        print("Média inválida")
elif type == "p":
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    p1 = int(input())
    p2 = int(input())
    p3 = int(input())
    mp = (((n1*p1) + (n2*p2) + (n3*p3)) / (p1 + p2 + p3))
    print ("{:.2f}".format(mp))
    if 70 <= mp <= 100:
        print("Aprovado")
    elif 0 < mp < 40:
        print("Reprovado")
    elif 40 <= mp <= 70:
        print("Final")
    else:
        print("Média inválida")
elif type == "h":
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    mh = (3/(1/n1+1/n2+1/n3))
    print ("{:.2f}".format(mh))
    if 70 <= mh <= 100:
        print("Aprovado")
    elif 0 < mh < 40:
        print("Reprovado")
    elif 40 <= mh <= 70:
        print("Final")
    else:
        print("Média inválida")
else:
    print("Escolha um tipo de media valida.")


