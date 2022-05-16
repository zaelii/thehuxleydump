while True:
    entrada = input()
    if entrada == "FIM":
        break
    l1, l2, l3 = map(int, entrada.split())

    if l1 >= l2 + l3 or l2 >= l1 + l3 or l3 >= l2 + l1:
        print ("INVALIDO")
    else:
        if l1 == l2 and l2 == l3:
            print("EQUILATERO")
        elif l1 != l2 and l2 != l3:
            print("ESCALENO")
        else:
            print("ISOSCELES")
           
#UNDONE 19OKS 2ERRORS
