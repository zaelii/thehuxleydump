n1 = int(input())
n2 = int(input())
n3 = int(input())

media = ((n1 + n2 + n3) / (3))

if 70 <= media < 100:
    print("A media do aluno foi {:.2f}".format (media) + " e ele foi APROVADO")
elif 0 < media <= 40:
    print("A media do aluno foi {:.2f}".format (media) + " e ele foi REPROVADO")
elif 40 < media < 70:
    print("A media do aluno foi {:.2f}".format (media) + " e ele foi FINAL")
else:
    print ("Media invalida")
