n1 = float(input())
n2 = float(input())
n3 = float(input())
p1 = float(input())
p2 = float(input())
p3 = float(input())

ma = (n1+n2+n3) / 3
mp = (((n1*p1) + (n2*p2) + (n3*p3)) / (p1 + p2 + p3))
mh = (3/(1/n1+1/n2+1/n3))

print ("a: ""{:.1f}".format(ma))
print ("p: ""{:.1f}".format(mp))
print ("h: ""{:.1f}".format(mh))
