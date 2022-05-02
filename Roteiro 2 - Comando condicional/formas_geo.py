from re import X


formageo = input()
pi = 3.14

if formageo == "Q":
    lq = float(input())
    areaq = lq ** 2
    perq = lq * 4
    print ("{:.2f}".format(areaq)) 
    print ("{:.2f}".format(perq))
if formageo == "R":
    lr = float(input())
    hr = float(input())
    largr = lr * hr
    altr = 2*(lr+hr)
    print ("{:.2f}".format(largr)) 
    print ("{:.2f}".format(altr))
if formageo == "C":
    raio = float(input())
    areac = pi * raio**2
    compc = 2*pi*raio
    print ("{:.2f}".format(areac)) 
    print ("{:.2f}".format(compc))
if formageo != "Q" and formageo != "R" and formageo != "C":
    print("Nenhuma figura selecionada")

    