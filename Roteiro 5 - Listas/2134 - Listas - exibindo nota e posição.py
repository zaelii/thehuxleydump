notas = []
quantas_notas = int(input())
ordem = 1

if quantas_notas <= 0 or quantas_notas >= 5:
    print("Numero de notas invalido.")
else:
    while(quantas_notas > 0):
        nota = float(input())
        print("Nota {}: {}".format(ordem,nota))
        notas.append(nota)
        quantas_notas = quantas_notas-1
        ordem = ordem +1

    media = sum(notas)/len(notas)
    print("Média: {:.2f}".format(media))

