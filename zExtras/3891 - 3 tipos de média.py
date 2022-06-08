nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

media = (nota1 + nota2 + nota3)/3
mediapond1 = (nota1*2 + nota2*2 + nota3*3)/(2+2+3)
mediapond2 = (nota1*1 + nota2*2 + nota3*2)/(1+2+2)

print("{:.2f}".format(media))
print("{:.2f}".format(mediapond1))
print("{:.2f}".format(mediapond2))