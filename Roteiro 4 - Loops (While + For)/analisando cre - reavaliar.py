cre_acumulado = 0
n_alunos = 0
matriculas = []
notas = []


while True:
    matricula = int(input())
    matriculas.append(matricula)
    if matricula == 999:
        break
    cre = float(input())
    notas.append(cre)

    n_alunos += 1
    cre_acumulado += cre


##extraindo resultados
media = cre_acumulado/n_alunos
posicao_menor_nota = notas.index(min(notas))
pos = matriculas[posicao_menor_nota]



print(pos)
print("{:.2f}".format(media))




